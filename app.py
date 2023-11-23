from flask import Flask, render_template, request, redirect, url_for
from utils import generate_activation_code
from database import UserDB
from email_service import send_activation_email

app = Flask(__name__)
user_db = UserDB()

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Generate activation code
        activation_code = generate_activation_code()

        # Save user details to the database
        user_db.add_user(email, password, activation_code)

        # Send activation email
        send_activation_email(email, activation_code)

        return "Registration successful! Please check your email to activate your account."
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
