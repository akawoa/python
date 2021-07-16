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

@app.route('/edit/<idFromURL>')
def edit(idFromURL):
    searchForThis = int(idFromURL)
    id_data = {
        'id': searchForThis
    }
    user = User.select_one(id_data)
    print(user.id)
    return render_template('edit.html', idFromURL=user.id)

@app.route('/editprocess/<idFromURL>', methods=["POST"])
def edituser(idFromURL):
    idFromURL = int(idFromURL)
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id" : idFromURL
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.edit(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/delete/<idFromURL>')
def delete(idFromURL):
    searchForThis = int(idFromURL)
    id_data = {
        'id': searchForThis
    }
    user = User.delete(id_data)
    return redirect('/')

@app.route('/view/<idFromURL>')
def view(idFromURL):
    searchForThis = int(idFromURL)
    data = {
        'id': searchForThis
    }
    user = User.select_one(data)
    return render_template('view.html', single_user = user)
            
if __name__ == "__main__":
    app.run(debug=True)