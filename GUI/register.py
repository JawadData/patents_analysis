from flask import Flask, request, render_template, jsonify, send_file
import mysql.connector
import logging

app = Flask(__name__)

# MySQL configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "...",
    "database": "..."  # Replace with your database name
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

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
    
    csv_file_path = 'data\\datasets\\ES.csv'

   
    return send_file(csv_file_path, as_attachment=True)


@app.route('/LOADGP')
def LOADGP():
    
    csv_file_path = 'data\\datasets\\GP.csv'

    
    return send_file(csv_file_path, as_attachment=True)


@app.route('/LOADWIPO')
def LOADWIPO():
    
    csv_file_path = 'data\\datasets\\WIPO.csv'

    
    return send_file(csv_file_path, as_attachment=True)


@app.route('/LOADFPO')
def LOADFPO():
    
    csv_file_path = 'data\\datasets\\FPO.csv'

    
    return send_file(csv_file_path, as_attachment=True)


@app.route('/LOADCND')
def LOADCND():
    
    csv_file_path = 'data\\datasets\\CND.xlsx'

    
    return send_file(csv_file_path, as_attachment=True)


@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']

    cursor = conn.cursor()
    
    query_check_user = "SELECT COUNT(*) FROM Users WHERE FirstName = %s OR LastName = %s OR Email = %s"
    cursor.execute(query_check_user, (firstname, lastname, email))
    result = cursor.fetchone()

    if result[0] > 0:
        
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
        
        cursor.close()
        message = "Login successful"
        success = True
    else:
        
        cursor.close()
        message = "Invalid username/email or password"
        success = False

    return jsonify({'message': message, 'success': success})


if __name__ == '__main__':
    app.run(debug=True)
