'''
Devo Council - Tawab Berri, Ivan Gontchar, Nia Lam, Alex Luo
SoftDev
2024-10-29
p00 - Scenario Two - Blog Website
time spent: 0 hrs
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
# add more data rows as needed
db.commit()


# @app.route(("/"), methods=['GET', 'POST'])
# def home():
#     if 'username' in session:
#         return "Welcome back " + session['username']
#     return "Hello Stranger."

@app.route(("/"), methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template( 'home.html' )
    return redirect(url_for('login'))

@app.route(("/login") , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("HELLo")
        # ...then we put their username into our session
        session['username'] = request.form['username']

        newdata = [request.form['username'], request.form['password'], os.urandom(32)]
        c.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?);", newdata); 
        db.commit()

        #PRINT STATEMENT
        c.execute('SELECT * FROM users;')
        result = c.fetchall()
        print("USERS:")
        for row in result:
            print(result)
        
        # we tried this print below because we thought that request.cookies.get
        # was equivalent to request.form, based on the notes, however, this prints
        # "None". Perhaps the notes implied that by function it would be the same
        # but there are extra steps to set up the cookies
        # print(request.cookies.get('username'))

        # print(session['username'])

        # since user inputed something, send them to the response page
        return redirect(url_for('home'))

    # otherwise we display the login page
    print("HI")
    return render_template( 'login.html' )

@app.route("/response", methods=['GET', 'POST'])
def response():
    # if we have info on the person, aka their username...
    if 'username' in session:
        # if there is a submission with post...
        if request.method == 'POST':
            # ...then the user pressed the button to logout, and we send them to the logout page
            return redirect(url_for('logout'))
        # otherwise we display the response page
        return render_template( 'home.html', username = session['username'])
    # this is something we added in later since we noticed if someone tried to be
    # sneaky and add response to the url from say the home page, it would give an error because there was
    # no username in session, so if they try that without any input, they get sent
    # back to the login screen
    return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    # if we have info on the person, aka their username...
    if 'username' in session:
        # if there is a submission with post...
        if request.method == 'POST':
            # if they pressed the submission named "logout"...
            if request.form.get("logout") is not None:
                # ...then the user is logging out, and we take their info out of the session...
                session.pop('username', None)
                # ... and then we send them back to the login page
                return redirect(url_for('login'))
            # ...otherwise they pressed the submission named "back"...
            else:
                # ...and then we send them back to the response page
                return redirect(url_for('response'))
        # send them back to the login page
        return render_template( 'logout.html', username = session['username'])
    # this is something we added in later since we noticed if someone tried to be
    # sneaky and add logout to the url, it would give an error because there was
    # no username in session, so if they try that without any input, they get sent
    # back to the login screen
    return redirect(url_for('login'))


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
