import sqlite3 #stdlib
from hashlib import sha256 #stdlib

DATABASE = 'data/database.db' #from prospective of app.py

def setup():
    """Creates the database and adds the user account credentials table and politician activity table."""
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command =  "CREATE TABLE IF NOT EXISTS credentials (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)"
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS politicians (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, politician_name TEXT NOT NULL)"
    c.execute(command)
    db.commit()
    db.close()

#============================ Adding Into Database ============================

def add_user(username,password):
    '''Takes in the username and password and adds
    it into the database table "credentials".'''
    password = sha256(password.encode('utf-8')).hexdigest()
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command = "INSERT INTO credentials (username,password)VALUES(?,?);"
    c.execute(command,(username,password))
    db.commit()
    db.close()
#============================ Getting From Database ============================

def get_username_list():
    '''Returns the list of all usernames.'''
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command = "SELECT username FROM credentials;"
    c.execute(command)
    output = c.fetchall()
    db.close()
    user_list = []
    for user in output:
        user_list.append(user[0])
    return user_list

def follow(user_id, politician_name):
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command = 'INSERT INTO politicians (user_id, politician_name) VALUES (?, ?)'
    c.execute(command,(str(user_id), politician_name))
    db.commit()
    db.close()

def unfollow(user_id, politician_name):
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command = 'DELETE FROM politicians WHERE user_id = ? AND politician_name = ?'
    c.execute(command, (str(user_id), politician_name))
    db.commit()
    db.close()

def get_followed(user_id):
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command = 'SELECT politician_name FROM politicians WHERE user_id = ?'
    c.execute(command, (str(user_id)))
    output = c.fetchall()
    # print(output)
    db.close()
    return output

# setup()
# get_followed('1')

def authenticate(username, pw):
    """Returns True if given username and password match. Otherwise return False."""
    pw = sha256(pw.encode('utf-8')).hexdigest()
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command = "SELECT * FROM credentials WHERE username='{}' AND password='{}'".format( username, pw )
    c.execute(command)
    retBool = c.fetchone() != None
    db.close()

    return retBool

def getIDFromUsername(username):
    """Returns the primary key ID of an account given a username."""
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command = "SELECT id FROM credentials WHERE username='{}'".format( username )
    c.execute(command)
    userID = c.fetchone()[0]
    db.close()

    return userID
