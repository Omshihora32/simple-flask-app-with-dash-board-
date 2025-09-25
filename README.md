# simple-flask-app-with-dash-board-

🔹 Flask Imports
1. Flask

Main class to create a web application.

You create an app object using app = Flask(__name__).

2. render_template

Renders an HTML file from the templates/ folder.

Example: Returning a login page or dashboard.

3. request

Handles data sent from the client (like form data, URL params, or JSON).

Example: request.form.get("username") gets input from an HTML form.

4. redirect

Sends the user to another route/page.

Example: After login, redirect the user to a dashboard page.

5. url_for

Dynamically generates URLs for routes using function names.

Safer than hardcoding paths.

6. session

Stores data per user across requests (uses secure cookies).

Example: Keeps track of a logged-in user until they log out.

🔹 Other Python Modules
7. json

Used for reading/writing JSON data (APIs, config, storage).

8. os

Lets you interact with the operating system.

Example: Work with file paths, check environment variables, etc.
