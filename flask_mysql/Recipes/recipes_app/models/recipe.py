# import the function that will return an instance of a connection
from recipes_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from recipes_app import app
import re
bcrypt = Bcrypt(app)

LETTERS_ONLY_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_thirty = data['under_thirty']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database for all Dojos

    @classmethod
    def get_recipe_by_id(cls, data):
        query = "SELECT * from recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        resultObject = cls(results[0])
        print (resultObject)
        return resultObject
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        # Create an empty list to append our instances of recipes
        recipes = []
        # Iterate over the db results and create instances of recipes with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes (name, description, instructions, under_thirty, created_at, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_thirty)s, %(created_at)s, %(user_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('recipes_schema').query_db( query, data )

    #Class method to delete a single recipe
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('recipes_schema').query_db( query, data )

    @classmethod
    def edit(cls, data ):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s,under_thirty = %(under_thirty)s, created_at = %(created_at)s WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('recipes_schema').query_db( query, data )

    @staticmethod
    def validate_recipe(recipe):

        #Name Validation
        is_valid = True
        if len(recipe['name']) == 0:
            flash("Recipe name required.", "name")
            is_valid = False
        elif len(recipe['name']) < 3:
            flash("Recipe name must be at least 3 characters in length", "name")
            is_valid = False

        #Description Validation
        is_valid = True
        if len(recipe['description']) == 0:
            flash("Description required.", "description")
            is_valid = False
        elif len(recipe['description']) < 3:
            flash("Description must be at least 3 characters in length", "description")
            is_valid = False

        #Instructions Validation
        is_valid = True
        if len(recipe['instructions']) == 0:
            flash("Instructions are required.", "instructions")
            is_valid = False
        elif len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters in length", "instructions")
            is_valid = False

        #Date Validation
        if len(recipe['created_at']) == 0:
            flash("Created at field is required for registration.", "created_at")
            is_valid = False
        return is_valid