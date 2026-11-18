from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",        # MySQL host
    user="root",             # MySQL username
    password="",             # MySQL password 
    database="online_bookstore"  
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Insert the user into the database without hashing the password
        cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, 'customer')", 
                       (name, email, password))
        db.commit()

        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        # Directly compare the stored password with the input password (no hashing)
        if user and user[3] == password:  # user[3] is the password column
            return redirect(url_for('index'))  # Redirect to home page after successful login
        else:
            return "Invalid credentials!"
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
