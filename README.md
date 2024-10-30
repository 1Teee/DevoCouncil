# Scenario Two by DevoCouncil
## Tawab Berri, Nia Lam, Ivan Gontchar, Alex Luo
### Target Ship Date: {2024-11-08}
<br>
<b>Description of Project: </b> 
The website is used for minimalistic blogging purposes. Once users register for an account and log in, users will be able to create/edit their own blogs and read other users' blogs. A search bar will be provided to navigate and search through the blogs.
</br>
<br>
<b>Roles: </b>

Tawab (PM): Back End(SQLITE/databases)
Facilitate storage of blog private keys in user’s profile (to allow edit access and viewing of past entries) 
Facilitate storage of blog entries as list items connected to the keys in the user's profile

Ivan: Back End(SQLITE/databases)
Facilitate storage of all blog entries in the table, with their unique attributes that will correlate them to given users, and store their information

Alex: Front End (HTML+CSS)
Implement HTML structure and CSS styling for the home page
Style welcome banner, navigation links, search bar, and indicator of login status
Create layout for registration/login and personal blogs/other blogs
Style search results page

Nia: Middleware (Flask, Python) + HTML
Facilitate user sessions/accounts and permissions (admin or user, usernames and passwords, login/logout and signup)
</br>
<br>
<b>Install guide:</b> 
<p>1) Open terminal and nav to directory where you want to place files</p>
<p>2)  clone the repo with:</p>
<p><code>git clone https://github.com/1Teee/DevoCouncil.git</code></p>
<p>3) cd into the repo </p>
<p>4) setup a virtual environment</p>
<p><code>python3 -m venv foo</code></p>
<p> 5) activate virtual environment</p>
<p><code>source foo/bin/activate</code></p>
<p>6) install required packages</p>
<p><code>pip install -r requirements.txt</code></p>
</br>
<b>Launch codes: </b> 
<p>1) start the server with:</p>
<p><code>python3 app.py</code></p>
<p>2) Open firefox and go to <code>http://127.0.0.1:5000</code></p>
