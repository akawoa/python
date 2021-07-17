from flask import render_template, redirect, request

from flask_app import app
# import the class from friend.py
from flask_app.models.dojo import Dojo

@app.route('/')
def dojo_index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)

@app.route('/process_dojo', methods=["POST"])
def create_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "dname": request.form["dname"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Dojo.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route('/viewdojo/<idFromURL>')
def view_dojo_test(idFromURL):
    searchForThis = int(idFromURL)
    data = {
        'id': searchForThis
    }
    single_dojo = Dojo.select_dojo(data)
    return render_template('ninja_index.html', single_dojo = single_dojo)