from flask import render_template, redirect, request

from flask_app import app
# import the class from friend.py
from flask_app.models.ninja import Ninja

@app.route('/ninja')
def index():
    users = Ninja.get_all()
    print(users)
    return render_template("ninja_index.html", all_users = users)

@app.route('/create_ninja/process', methods=["POST"])
def create_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"],
        "image" : request.form["image"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Ninja.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/create_ninja')
def form():
    return render_template('ninja_form.html')

@app.route('/ninja/edit/<idFromURL>')
def edit(idFromURL):
    searchForThis = int(idFromURL)
    id_data = {
        'id': searchForThis
    }
    user = Ninja.select_one(id_data)
    print(user.id)
    return render_template('edit.html', idFromURL=user.id)

@app.route('/ninja/editprocess/<idFromURL>', methods=["POST"])
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
    Ninja.edit(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/ninja/delete/<idFromURL>')
def delete(idFromURL):
    searchForThis = int(idFromURL)
    id_data = {
        'id': searchForThis
    }
    user = Ninja.delete(id_data)
    return redirect('/')

@app.route('/view/<idFromURL>')
def view_dojo(idFromURL):
    searchForThis = int(idFromURL)
    data = {
        'id': searchForThis
    }
    single_dojo = Ninja.select_dojo(data)
    print(single_dojo[0])
    return render_template('ninja_index.html', single_dojo = single_dojo)