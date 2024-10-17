from flask import Flask, request, render_template, jsonify, send_file
import mysql.connector
import logging

app = Flask(__name__)

# MySQL configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "id1fs",
    "database": "patent"  # Replace with your database name
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# SQL statement to create the Users table
create_table_query = """
CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Execute the create table query
cursor.execute(create_table_query)
conn.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acceuil')
def acceuil():
    return render_template('acceuil.html')


@app.route('/CND-DASH')
def Canadian():
    return render_template('CND-DASH.html')


@app.route('/Canadian')
def CND():
    return render_template('Canadian.html')


@app.route('/ESP-DASH')
def Espace():
    return render_template('ESP-DASH.html')


@app.route('/Espace')
def ESP():
    return render_template('Espace.html')


@app.route('/GP')
def google_patents():
    return render_template('GP.html')


@app.route('/google_patents')
def GP():
    return render_template('google_patents.html')


@app.route('/FPO-DASH')
def FPO():
    return render_template('FPO-DASH.html')


@app.route('/FPO')
def FPPO():
    return render_template('FPO.html')


@app.route('/wipo')
def wipo():
    return render_template('wipo.html')


@app.route('/WIPO-DASH')
def WIPO_DASH():
    return render_template('WIPO-DASH.html')


@app.route('/LOADESP')
def LOADESP():
    # Path to the CSV file
    csv_file_path = 'data\\datasets\\ES.csv'

    # Send the file to the user
    return send_file(csv_file_path, as_attachment=True)


@app.route('/LOADGP')
def LOADGP():
    # Path to the CSV file
    csv_file_path = 'data\\datasets\\GP.csv'

    # Send the file to the user
    return send_file(csv_file_path, as_attachment=True)


@app.route('/LOADWIPO')
def LOADWIPO():
    # Path to the CSV file
    csv_file_path = 'data\\datasets\\WIPO.csv'

    # Send the file to the user
    return send_file(csv_file_path, as_attachment=True)


@app.route('/LOADFPO')
def LOADFPO():
    # Path to the CSV file
    csv_file_path = 'data\\datasets\\FPO.csv'

    # Send the file to the user
    return send_file(csv_file_path, as_attachment=True)


@app.route('/LOADCND')
def LOADCND():
    # Path to the CSV file
    csv_file_path = 'data\\datasets\\CND.xlsx'

    # Send the file to the user
    return send_file(csv_file_path, as_attachment=True)


@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']

    cursor = conn.cursor()
    # Check if user already exists
    query_check_user = "SELECT COUNT(*) FROM Users WHERE FirstName = %s OR LastName = %s OR Email = %s"
    cursor.execute(query_check_user, (firstname, lastname, email))
    result = cursor.fetchone()

    if result[0] > 0:
        # User already exists
        cursor.close()
        message = "User Already Exists"
        success = False
        return jsonify({'message': message, 'success': success})

    query = "INSERT INTO Users (FirstName, LastName, Email, Password) VALUES (%s, %s, %s, %s)"
    values = (firstname, lastname, email, password)

    try:
        cursor.execute(query, values)
        conn.commit()
        logging.debug(f"User {firstname} {lastname} registered successfully")
        message = "Registration successful"
        success = True
    except mysql.connector.Error as err:
        logging.error(f"Error: {err}")
        conn.rollback()
        message = f"An error occurred: {err}"
        success = False
    finally:
        cursor.close()

    return jsonify({'message': message, 'success': success})


@app.route('/login', methods=['POST'])
def login():
    username_or_email = request.form['username_or_email']
    password = request.form['password']

    cursor = conn.cursor()
    query_check_user = "SELECT COUNT(*) FROM Users WHERE (FirstName = %s OR Email = %s) AND Password = %s"
    cursor.execute(query_check_user, (username_or_email, username_or_email, password))
    result = cursor.fetchone()

    if result[0] > 0:
        # User exists and password is correct
        cursor.close()
        message = "Login successful"
        success = True
    else:
        # User does not exist or password is incorrect
        cursor.close()
        message = "Invalid username/email or password"
        success = False

    return jsonify({'message': message, 'success': success})


if __name__ == '__main__':
    app.run(debug=True)
