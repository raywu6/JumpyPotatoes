import sqlite3 #stdlib

DATABASE = 'data/database.db' #from prospective of app.py

def setup():
    """Creates the database and adds the user account credentials table and politician activity table."""
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS credentials (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)"
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS politician_activity (id INTEGER PRIMARY KEY AUTOINCREMENT, politician_name TEXT NOT NULL UNIQUE, number_articles INTEGER NOT NULL, number_media_outlets INTEGER NOT NULL)"
    c.execute(command)
    db.commit()
    db.close()
