import os #stdlib

from flask import Flask, render_template, session, redirect, request, flash, url_for #pip install flask

from util import database, api, fortune

import pprint

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/')
def home():
    #print(news_api.nyt_news("W"))
    #pp = pprint.PrettyPrinter(indent=4)
    civic_list = []
    if 'civic_list' in session:
        civic_list = session['civic_list']
        session.pop('civic_list')
    else:
        civic_list = api.civic(10282)
    # news_list = []
    msg = ''
    type = 'primary'
    if 'msg' in session:
        msg = session['msg']
        type = session['type']
        session.pop('msg')
        session.pop('type')
    if 'follow' in request.args:
        database.follow(session['id'], request.args['follow'])
        msg = 'You have successfully followed ' + request.args['follow']
        type = 'success'
    if 'unfollow' in request.args:
        database.unfollow(session['id'], request.args['unfollow'])
        msg = 'You have successfully unfollowed ' + request.args['unfollow']
        type = 'success'
    quote = fortune.getQuote()
    followed = []
    if 'id' in session:
        data = database.get_followed(session['id'])
        for row in data:
            followed.append(row[0])
    #print(civic_list)
    return render_template("index.html", s = session, l = civic_list, c = len(civic_list), m = msg, t = type, q = quote, f = followed)

@app.route("/search", methods=["GET"])
def search():
    '''redirects search appropriately based on what was searched for'''
    zip = str(request.args.get('search'))
    if (len(zip) == 5):
        return redirect("politicians/" + zip)
    else:

        flash('Please insert a valid zip code', 'danger')
        return redirect('/')

@app.route("/politicians/<int:zip>")
def politicians(zip):
    session['civic_list'] = api.civic(zip)
    # news_list = []
    if session['civic_list'] == "error":
        session.pop('civic_list')
        print ("nope. error on google api")
        session['msg'] = "Invalid search query!"
        session['type'] = 'danger'
    return redirect( url_for('home') )

@app.route("/politicianpage/<name>")
def politicianpage(name):
    artNYT = api.nyt_news(name)
    artNews = api.news_api(name)

    if len(artNYT) > 5:
        lenNYT = 5
    else:
        lenNYT = len(artNYT)

    if len(artNews) > 5:
        lenNews = 5
    else:
        lenNews = len(artNews)

    topArtNYT = artNYT[0 : lenNYT]
    topArtNews = artNews[0 : lenNews]

    print ('\n\n\n' + str(topArtNYT) + '\n\n\n')
    print ('\n\n\n' + str(topArtNews) + '\n\n\n')

    return render_template('politician.html', name=name , articles_nyt = topArtNYT , articles_news = topArtNews )


def is_logged_in():
    '''Returns True if the user is logged in. False otherwise.'''
    return "id" in session

@app.route("/login", methods=['GET'])
def login():
    '''Redirects to the homepage if the user is logged in. Displays the login page if the user is not logged in.'''
    if (is_logged_in()):
        return redirect(url_for("home"))
    msg = ''
    type = ''
    if 'msg' in request.args:
        msg = 'Please Login Before Following a Politician.'
        type = 'warning'
    if 'msg' in session:
        msg = session['msg']
        type = session['type']
        session.pop('msg')
        session.pop('type')
    return render_template("login.html", m = msg, t = type)

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
    msg = ''
    type = 'primary'
    if (submit_type == "Register"):
        username_input = request.form.get("username")
        password_input = request.form.get("password")
        c_password_input = request.form.get("confirm_password")
        if (len(username_input.replace(" ","")) < 4):
            msg = "Username has to be at least 4 characters long."
            type = 'danger'
        elif (len(password_input.replace(" ","")) < 4):
            msg = "Password has to be at least 4 characters long."
            type = 'danger'
        elif username_input in username_list:
            msg = "Username already exists. Please try a different username."
            type = 'danger'
        #check that password confirm
        elif (password_input != c_password_input):
            msg = "Password and Confirm Password do not match."
            type = 'danger'
        else:
            database.add_user(username_input,password_input)
            session['msg'] = "Successfully created account."
            session['type'] = 'success'
            return redirect(url_for("login"))
        return render_template("register.html", m = msg, t = type)
    elif (submit_type == "Login"):
        username_input = request.form.get("username")
        password_input = request.form.get("password")
        if (username_input in username_list):
            if (database.check_password(username_input,password_input)):
                session['msg'] = "Successfully Logged In."
                session['type'] = 'success'
                session["id"] = database.get_id_from_username(username_input)
                return redirect(url_for("home"))
        msg = "Username or password is incorrect. Please try again."
        type = 'danger'
        return render_template("login.html", m = msg, t = type)
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    '''Removes the current session and redirects users back to login page.'''
    session.pop("id")
    session['msg'] = "Successfully Logged Out"
    session['type'] = 'success'
    return redirect('/')

if __name__ == '__main__':
    app.debug = True #set to False in production mode
    database.setup()
    app.run()
