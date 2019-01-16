import sqlite3 #stdlib

from flask import session #pip install flask

from . import database as dtb #relative import

DATABASE_LINK = "data/database.db" #from prospective of app.py

def is_logged_in():
    """Returns True if a username is in session, false otherwise."""
    return 'id' in session

def login(username, pw):
    """If credentials match, add the user ID to the session and return True. Otherwise return False."""
    if dtb.authenticate(username, pw):
        session['id'] = dtb.getIDFromUsername(username)
        return True
    else:
        return False

def logout():
    """Removes the current session."""
    if is_logged_in():
        session.pop('id')
        return True
    return False

def getID():
    """Returns the user ID stored in the current session."""
    return session['id']

def getUsername():
    """Returns the username of the current logged in session."""
    try:
        db = sqlite3.connect('data/data.db')
        c = db.cursor()
        command = "SELECT username FROM credentials WHERE id={}".format( session['id'] )
        c.execute(command)
        username = c.fetchone()[0]
        db.close()

        return username
    
    except KeyError:
        return None #not logged in
