import os #stdlib

from flask import Flask, render_template, session, redirect, request, flash, url_for #pip install flask

from util import database

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/')
def home():
    return render_template("index.html")

def is_logged_in():
    '''Returns True if the user is logged in. False otherwise.'''
    return "id" in session

@app.route("/login")
def login():
    '''Redirects to the homepage if the user is logged in. Displays the login page if the user is not logged in.'''
    if (is_logged_in()):
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register")
def register():
    '''Display the register page.'''
    if (is_logged_in()):
        redirect(url_for("home"))
    return render_template("register.html", isLoggedIn = is_logged_in())

@app.route("/auth", methods=["POST"])
def authenticate():
    '''Handles the information that the user submits for either logging in or
    registering. It will redirect the user to the appropriate pages and flash
    messages if there are errors.'''
    submit_type = request.form.get("submit")
    username_list = database.get_username_list()
    if (submit_type == "Register"):
        username_input = request.form.get("username")
        password_input = request.form.get("password")
        c_password_input = request.form.get("confirm_password")
        if (len(username_input.replace(" ","")) < 4):
            flash("Username has to be at least 4 characters long.","error")
        elif (len(password_input.replace(" ","")) < 4):
            flash("Password has to be at least 4 characters long.","error")
        elif username_input in username_list:
            flash("Username already exists. Please try a different username.","error")
        #check that password confirm
        elif (password_input != c_password_input):
            flash("Password and Confirm Password do not match.","error")
        else:
            database.add_user(username_input,password_input)
            flash("Successfully created account.","success")
            return redirect(url_for("login"))
        return redirect(url_for("register"))
    elif (submit_type == "Login"):
        print('asda')
        username_input = request.form.get("username")
        password_input = request.form.get("password")
        if (username_input in username_list):
            if (database.check_password(username_input,password_input)):
                session["id"] = database.get_id_from_username(username_input)
                return redirect(url_for("home"))
        flash("Username or password is incorrect. Please try again.","error")
        return redirect(url_for("login"))
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    '''Removes the current session and redirects users back to login page.'''
    if (is_logged_in()):
        session.pop("id")
        return redirect(url_for("login"))
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.debug = True #set to False in production mode
    app.run()
