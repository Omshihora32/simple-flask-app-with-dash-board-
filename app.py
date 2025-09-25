from flask import Flask , render_template , request , redirect , url_for , session
import json
import os

app = Flask(__name__)
app.secret_key = "Team"

@app.route("/" , methods = ["POST" , "GET"])
def register():
    # error is empty set here
    errors = {}
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        cpassword = request.form.get("cpassword")
        email = request.form.get("email")

        # --- VALIDATION LOGIC START ---

        if not username:
            errors['username'] = 'Username cannot be empty. Please choose a username.'
        if not password or len(password) < 6:
            errors['password'] = 'Password must be at least 6 characters long.'
        if not name:
            errors['name'] = 'name cannot be empty.'
        if not cpassword or cpassword != password:
            errors['cpassword'] = 'password not matched.'

        # --- VALIDATION LOGIC END ---

        if not errors:
            new_user = {'username' : username , 'password' : password , 'email' : email}
            data_path = os.path.join(os.path.dirname(__file__), "data.json")
            try:
                with open(data_path) as fs:
                    users = json.load(fs)
            except(FileNotFoundError , json.JSONDecodeError):
                users = []
            users.append(new_user)

            with open(data_path , 'w') as fs:
                json.dump(users , fs , indent=4)
            print(f"User '{username}' successfully registered and saved.")
            return render_template("login.html" ,errors=errors , success_massage = "Registration successfully!")

        return render_template("register.html" , errors = errors , username = username)
    
    return render_template('register.html', errors=errors)

@app.route("/login" , methods = ["POST" , "GET"])
def login():
    errors = {}
    username = ""
    password = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

    if not username:
            errors['username'] = 'Username cannot be empty. Please choose a username.'
    if not password or len(password) < 6:
            errors['password'] = 'Password must be at least 6 characters long.'

    if not errors:
        data_path = os.path.join(os.path.dirname(__file__), "data.json")
        try:
            with open(data_path) as fs:
                users = json.load(fs)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []

        dummy_data = [i for i in users if i['username'] == username and i['password'] == password]

        if not dummy_data:
            errors['eusername'] = 'User not found or incorrect password. Please register first.'
            return render_template("login.html" , errors = errors)
        session['username'] = username
        return render_template("dashboard.html" , errors = errors , username = username)
    return render_template("login.html" , errors = errors)
        

@app.route("/logout")
def logout():
    session.pop('username' , None)
    return redirect(url_for("login"))

#  that tells the computer to start the web server if you run this file directly.
if __name__ == '__main__':
    app.run(debug=True)