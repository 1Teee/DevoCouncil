'''
Devo Council - Tawab Berri, Ivan Gontchar, Nia Lam, Alex Luo
SoftDev
2024-10-29
p00 - Scenario Two - Blog Website
time spent: 2 hrs
'''
from flask import Flask, render_template, request, session, redirect, url_for

import sqlite3
import os

app = Flask(__name__)    #create Flask object
DB_FILE = "database.db" #create a database for private keys storage

# makin' a supa-secret key
app.secret_key = "1234"

db = sqlite3.connect(DB_FILE, check_same_thread=False) #open if file exists, otherwise create
c = db.cursor()  #facilitate db ops -- you will use cursor to trigger db events

#c.execute("DROP TABLE users;")
c.execute(
'''
CREATE TABLE IF NOT EXISTS users (
        name TEXT PRIMARY KEY,
        password TEXT,
        privatekey TEXT
        );
''')


c.execute(
'''
CREATE TABLE IF NOT EXISTS blogs (
        title TEXT PRIMARY KEY,
        summary TEXT,
        content TEXT,
        author TEXT,
        datePublished TEXT,
        userKey TEXT
        );
''')
# add more data rows as needed
db.commit()


@app.route(("/"), methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template( 'home.html' )
    return redirect(url_for('login'))

@app.route(("/login") , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']

        newdata = [request.form['username'], request.form['password'], os.urandom(32)]
        c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?);", newdata)
        db.commit()

        #PRINT STATEMENT
        c.execute('SELECT * FROM users;')
        result = c.fetchall()
        print("USERS:")
        for row in result:
            print(result)
        return redirect(url_for('home'))
    return render_template( 'login.html' )

@app.route("/createBlog", methods=['GET', 'POST'])
def blogCreate():
    if 'username' in session:
        if request.method == 'POST':
            # userKey = c.execute(f"SELECT privatekey FROM users WHERE name = {session['username']};")
            # blogData = [request.form['title'], request.form['summary'], request.form['content'], request.form['author'], request.form['datePublished'], userKey]
            # c.execute("INSERT INTO blogs VALUES (?, ?, ?, ?, ?, ?)", blogData)
            # db.commit()
            print("XYZ")
        return render_template( 'home.html', username = session['username'])
    return redirect(url_for('login'))

@app.route("/myBlogs", methods=['GET', 'POST'])
def editing():
    if 'username' in session:
        print("HEYO")
        # userKey = c.execute(f"SELECT privatekey FROM users WHERE name = {session['username']};")
        # c.execute(f'SELECT * FROM blogs WHERE userKey = {userKey};')
        # result = c.fetchall()
    return redirect(url_for('login'))

@app.route("/viewBlog", methods=['GET', 'POST'])
def blogView(title):
    if 'username' in session:
        print("HEYO")
        # c.execute(f'SELECT * FROM blogs WHERE title = {title};')
        # blogInfo = c.fetchall()
    return redirect(url_for('login'))

app.route("/allBlogs", methods=['GET', 'POST'])
def allBlogs():
    if 'username' in session:
        print("HEYO")
        # c.execute(f'SELECT * FROM blogs;')
        # blogs = c.fetchall()
    return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        if request.method == 'POST':
            if request.form.get("logout") is not None:
                session.pop('username', None)
                return redirect(url_for('login'))
            else:
                return redirect(url_for('blogCreate'))
        return render_template( 'logout.html', username = session['username'])
    return redirect(url_for('login'))


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()

db.close()
