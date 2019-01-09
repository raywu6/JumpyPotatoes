import sqlite3 #stdlib

DATABASE = 'data/database.db' #from prospective of app.py

def setup():
    """Creates the database and adds the user account credentials table and politician activity table."""
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command =  "CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE,password TEXT)"
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS politician_activity (id INTEGER PRIMARY KEY AUTOINCREMENT, politician_name TEXT NOT NULL UNIQUE, number_articles INTEGER NOT NULL, number_media_outlets INTEGER NOT NULL)"
    c.execute(command)
    db.commit()
    db.close()

#============================ Adding Into Database ============================

def add_user(username,password):
    '''Takes in the username and password and adds
    it into the database table "users".'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO users (username,password)VALUES(?,?);"
    c.execute(command,(username,password))
    db.commit()
    db.close()
#============================ Getting From Database ============================

def get_username_list():
    '''Returns the list of all usernames.'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT username FROM users;"
    c.execute(command)
    output = c.fetchall()
    db.close()
    user_list = []
    for user in output:
        user_list.append(user[0])
    return user_list

def check_password(username,password):
    '''Returns True if the password matches the password that is associated
    with the username in the database and False otherwise.'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT password FROM users WHERE username = ?;"
    c.execute(command,(username,))
    output = c.fetchall()
    db.close()
    return output[0][0] == password

def get_id_from_username(username):
    '''Returns the id given a username'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT id FROM users WHERE username = ?;"
    c.execute(command,(username,))
    output = c.fetchall()
    db.close()
    return output[0][0]
