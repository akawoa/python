from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)
app.secret_key = "Final Fantasy"

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/process', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/create_user')
def form():
    return render_template('form.html')
            
if __name__ == "__main__":
    app.run(debug=True)