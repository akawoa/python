from recipes_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from recipes_app.models.user import User
from recipes_app.models.recipe import Recipe

bcrypt = Bcrypt(app)

@app.route('/recipes/new')
def add_recipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }

    logged_in_user = User.get_user_by_id(data)

    if logged_in_user == False:
        return redirect('/')
    return render_template("add_recipe.html", user = logged_in_user)

@app.route('/create_recipe/process', methods=["POST"])
def create_recipe():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        "id": session["user_id"]
    }

    logged_in_user = User.get_user_by_id(user_data)

    if logged_in_user == False:
        return redirect('/')
    
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    print(logged_in_user.id)
    recipe_data = {
        "name": request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "under_thirty" : request.form["under_thirty"],
        "created_at" : request.form["created_at"],
        "user_id" : logged_in_user.id
    }
        # We pass the data dictionary into the save method from the Friend class.
    Recipe.save(recipe_data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dashboard')

@app.route('/recipes/<idFromURL>')
def view_recipe(idFromURL):
    searchForThis = idFromURL
    data = {
        'id': searchForThis
    }
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        "id": session["user_id"]
    }

    logged_in_user = User.get_user_by_id(user_data)

    if logged_in_user == False:
        return redirect('/')
    recipe = Recipe.get_recipe_by_id(data)
    return render_template("view_recipe.html", single_recipe = recipe, user = logged_in_user)


@app.route('/recipes/edit/<idFromURL>')
def edit_recipe_form(idFromURL):
    searchForThis = idFromURL
    data = {
        'id': searchForThis
    }
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        "id": session["user_id"]
    }

    logged_in_user = User.get_user_by_id(user_data)

    if logged_in_user == False:
        return redirect('/')
    recipe = Recipe.get_recipe_by_id(data)
    return render_template("edit_recipe.html", single_recipe = recipe, user = logged_in_user)

@app.route('/edit_recipe/process', methods=["POST"])
def edit_recipe():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        "id": session["user_id"]
    }

    logged_in_user = User.get_user_by_id(user_data)

    if logged_in_user == False:
        return redirect('/')
    
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/edit')
    print(logged_in_user.id)
    recipe_data = {
        "id": request.form["id"],
        "name": request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "under_thirty" : request.form["under_thirty"],
        "created_at" : request.form["created_at"]
    }
    print("Recipe Data:")
    print(recipe_data["under_thirty"])
    # We pass the data dictionary into the save method from the Friend class.
    Recipe.edit(recipe_data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dashboard')

@app.route('/recipes/delete/<idFromURL>',)
def delete_recipe(idFromURL):
    searchForThis = int(idFromURL)
    id_data = {
        'id': searchForThis
    }
    Recipe.delete(id_data)
    return redirect("/dashboard")
