from log_and_reg_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from log_and_reg_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/users')
def user_index():
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)

@app.route('/process', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    hashed_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email_address": request.form["email_address"],
        "password": hashed_password
    }

    session['user_id'] = User.save(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # Run the data through the login validator
    # If it returns false, redirect away.
    # If it doesn't return false, then it actually returned
    # the user from the database that is trying to log in
    # So we'll store its user id in session
    login_validation = User.validate_login(request.form)


    if not login_validation:
        return redirect('/')

    session['user_id'] = login_validation.id
    return redirect('dashboard')


    return

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }

    logged_in_user = User.get_user_by_id(data)

    if logged_in_user == False:
        return redirect('/')
    return render_template('dashboard.html', user = logged_in_user)

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')