from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify 

app = Flask(__name__)
app.secret_key = "mykey123"

# Database connection
def db_connector():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="khataplus"
    )

# Create user-specific table if not exists
def create_table_if_not_exists(fullname):
    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS `{fullname}` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            date DATE NOT NULL,
            amount DECIMAL(10,2) NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# ================== Routes ==================

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        fname = request.form["fname"].strip().lower()
        lname = request.form["lname"].strip().lower()
        fullname = f"{fname}_{lname}"
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            message = "Passwords didn't match!"
            return render_template("register.html", message=message)

        try:
            hashed_password = generate_password_hash(password)
            conn = db_connector()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registered (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    fname VARCHAR(100) NOT NULL,
                    lname VARCHAR(100) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute(
                "INSERT INTO registered (fname,lname,email,password) VALUES (%s,%s,%s,%s)",
                (fname, lname, email, hashed_password)
            )
            conn.commit()
            conn.close()

            # Log in user immediately after registration
            session['user'] = fullname
            return redirect(url_for('index'))

        except Exception as e:
            message = "Error: " + str(e)

    return render_template("register.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            conn = db_connector()
            cursor = conn.cursor()
            cursor.execute("SELECT fname, lname, password FROM registered WHERE email=%s", (email,))
            user = cursor.fetchone()
            conn.close()

            if user and check_password_hash(user[2], password):
                fullname = f"{user[0].lower()}_{user[1].lower()}"
                session['user'] = fullname
                return redirect(url_for('index'))
            else:
                message = "Invalid credentials."
        except Exception as e:
            message = "Error: " + str(e)

    return render_template("login.html", message=message)


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route("/index")
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")  # session accessible in template


@app.route("/add_entry", methods=["GET", "POST"])
def add_entry():
    if 'user' not in session:
        return redirect(url_for('login'))

    message = ""
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        amount = request.form["amount"]
        notes = request.form["notes"]

        fullname = session['user']
        create_table_if_not_exists(fullname)
        conn = db_connector()
        cursor = conn.cursor()

        try:
            cursor.execute(
                f"INSERT INTO `{fullname}` (name,date,amount,notes) VALUES (%s,%s,%s,%s)",
                (name, date, amount, notes)
            )
            conn.commit()
            message = "✅ Entry added successfully!"
        except Exception as e:
            message = "❌ Failed to add entry. " + str(e)
        finally:
            conn.close()

    return render_template("add_entry.html", message=message)


@app.route("/balances")
def balances():
    if 'user' not in session:
        return redirect(url_for('login'))

    fullname = session['user']
    conn = db_connector()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM `{fullname}`")
    entries = cursor.fetchall()
    conn.close()

    return render_template("balances.html", entries=entries)

@app.route("/users")
def users():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    fullname=session['user']

    conn = db_connector()
    cursor = conn.cursor()
    cursor.execute(f"SELECT Distinct name FROM `{fullname}`")
    users = cursor.fetchall()
    conn.close()

    # Combine first and last names for display
    names = [f"{u[0].capitalize()}" for u in users]

    return render_template("users.html", names=names)
 # make sure you import this at the top


    
    
@app.route("/api/user_details/<username>")
def api_user_details(username):
    if 'user' not in session:
        return {"error": "Unauthorized"}, 401

    fullname = session['user']
    conn = db_connector()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch records ordered by date DESC
    cursor.execute(f"SELECT * FROM `{fullname}` WHERE name=%s ORDER BY date DESC", (username,))
    records = cursor.fetchall()
    conn.close()

    return {"records": records}

@app.route("/delete_entry/<int:id>")
def delete_entry(id):
    if 'user' not in session:
        return redirect(url_for('login'))

    fullname = session['user']
    conn = db_connector()
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"DELETE FROM `{fullname}` WHERE id=%s", (id,))
        conn.commit()
        message = "✅ Entry deleted successfully!"
    except Exception as e:
        print(f"Error: {e}")
        message = "❌ Error deleting entry."
    finally:
        conn.close()

    return redirect(url_for("balances",message=message))

@app.route("/edit_entry/<int:id>", methods=["GET", "POST"])
def edit_entry(id):
    if 'user' not in session:
        return redirect(url_for('login'))

    fullname = session['user']
    conn = db_connector()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        # Get updated data from form
        name = request.form["name"]
        date = request.form["date"]
        amount = request.form["amount"]
        notes = request.form["notes"]

        try:
            cursor.execute(
                f"UPDATE `{fullname}` SET name=%s, date=%s, amount=%s, notes=%s WHERE id=%s",
                (name, date, amount, notes, id)
            )
            conn.commit()
            message = "✅ Entry updated successfully!"
        except Exception as e:
            print(f"Error: {e}")
            message = "❌ Error updating entry."
        finally:
            conn.close()

        return redirect(url_for("balances"))

    # GET request: fetch current record
    cursor.execute(f"SELECT * FROM `{fullname}` WHERE id=%s", (id,))
    record = cursor.fetchone()
    conn.close()

    return render_template("update.html", record=record)



@app.route("/reports", methods=["GET", "POST"])
def reports():
    if 'user' not in session:
        return redirect(url_for('login'))

    total_amount = None
    selected_date = None
    fullname = session['user']

    if request.method == "POST":
        selected_date = request.form["selected_date"]
        conn = db_connector()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            f"SELECT SUM(amount) AS total_amount FROM `{fullname}` WHERE DATE_FORMAT(date, '%Y-%m') = %s",
            (selected_date,)
        )
        result = cursor.fetchone()
        total_amount = result['total_amount'] if result and result['total_amount'] else 0
        conn.close()

    return render_template("reports.html", total_amount=total_amount, selected_month=selected_date)


# ================== Run App ==================
if __name__ == "__main__":
    app.run(debug=True)
