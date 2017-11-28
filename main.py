from flask import Flask, request, redirect, render_template
import os
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route('/', methods=['POST', 'GET'])

def index():
    
    return render_template('index.html', title = "User Signup")
def validate_userinfo():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ""
    password_error = ""
    email_error = ""
   
    if username == "":
        username_error = "Must enter a user name"
    elif " " in username:
        username_error = "User name cannot contain a space"
    elif len(username) > 20 or len(username) < 3:
        username_error = "User name must be betweeen 3 and 20 characters"
    
    if password == "":
        password_error = "Must enter a password"
    elif " " in password:
        password_error = "Password cannot contain a space"
    elif len(password) > 20 or len(password) < 3:
        password_error = "Password must be betweeen 3 and 20 characters"
    elif password != verify:
        password_error = "Passwords do not match"
    
    if email == "":
        email_error = "Must enter a valid email address"
    elif " " in email:
        email_error = "Email address cannot contain a space"
    elif len(email) > 20 or len(email) < 3:
        email_error = "Email address must be betweeen 3 and 20 characters"
    elif email.count("@") != 1 or email.count(".") != 1:
        email_error= "Invalid email address"
    
    if username_error or password_error or email_error:
        return render_template('index.html', title = "User Signup", username=username, password="", verify="", email=email, username_error=username_error, password_error=password_error, email_error=email_error)
    else:
        return redirect('/welcome?username={0}'.format(username))

@app.route('/welcome')
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)


app.run()
