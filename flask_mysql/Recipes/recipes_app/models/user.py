# import the function that will return an instance of a connection
from recipes_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from recipes_app import app
import re
bcrypt = Bcrypt(app)

LETTERS_ONLY_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email_address = data['email_address']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database for all Dojos

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * from users WHERE id = %(id)s;"

        results = connectToMySQL('recipes_schema').query_db(query, data)

        if len(results) > 0:
            return cls(results[0])
        else:
            return False


    @classmethod
    def check_email(cls, data):
        query = "SELECT * FROM users WHERE email_address = %(email_address)s;"

        results = connectToMySQL('recipes_schema').query_db(query, data)

        if len(results) == 0:
            return False
        else:
            return cls(results[0])

    @staticmethod
    def validate_user(user):

        # First Name Validation
        is_valid = True
        if len(user['first_name']) == 0:
            flash("First name required.", "first_name")
            is_valid = False
        elif len(user['first_name']) < 2:
            flash("First name must be at least 2 characters in legnth", "first_name")
            is_valid = False
        elif not LETTERS_ONLY_REGEX.match(user['first_name']):
            flash("First name must not contain non-alphabetic characters", "first_name")
            is_valid = False

        # Last Name Validation
        is_valid = True
        if len(user['last_name']) == 0:
            flash("Last name required.", "last_name")
            is_valid = False
        elif len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters in length", "last_name")
            is_valid = False
        elif not LETTERS_ONLY_REGEX.match(user['last_name']):
            flash("Last name must not contain non-alphabetic characters", "last_name")
            is_valid = False


        # Email Address Validation
        if len(user['email_address']) == 0:
            flash("Email address required.", "email_address")
            is_valid = False
        elif not EMAIL_REGEX.match(user['email_address']):
            flash("Invalid email format. Must meet username@email.com", "email_address")
            is_valid = False
        elif User.check_email(user):
            flash("A user with that email already exists.", "email_address")
            is_valid = False


        # Password Validation
        if len(user['password']) == 0:
            flash("Password field is required for registration.", "password")
            is_valid = False
        elif len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "password")
            is_valid = False
        elif user['password'] != user['confirm_password']:
            flash("Password must match Confirm Password", "password")
            is_valid = False

        # Confirm Password Validation
        if len(user['confirm_password']) < 8:
            flash("Password must be at least 8 characters.", "confirm_password")
            is_valid = False
        return is_valid


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name, last_name, email_address, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email_address)s, %(password)s, current_timestamp(), current_timestamp());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('recipes_schema').query_db( query, data )
    @staticmethod
    def validate_login(login_user):
        user_in_db = User.check_email(login_user)
        #Does a user in our database have that email?
        if not user_in_db:
            flash("Invalid email/password", "login_email")
            return False
        
        # Assuming that user does exist in our database, does their encrypted password match that user's password?
        if not bcrypt.check_password_hash(user_in_db.password, login_user['password']):
            flash("Invalid email/password", "login_email")
        return user_in_db