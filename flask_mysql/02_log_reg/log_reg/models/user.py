from log_reg.config.mysqlconnection import connectToMySQL
from flask import flash
import re

LETTERS_ONLY_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX =  re.compile()


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated at)" VALUES ( %())

        return connectToMySQL('logregdemo').query_db(query, data)
    
    @staticmethod
    def validate_registration(user):
        is_valid = True

        #first name
        #submission required - make sure it's not an empty string
        if len(user['first_name']) == 0:
            flash("First name is required.", "first_name")
            is_valid = False
        #at least 2 characters
        elif len(user['first_name']) < 2:
            flash("first name must be at least 2 characters in length.", "first_name")
            is_valid = False
        #letters only
        elif not str.isalpha(user['first_name']):
            flash("first name must not contain non-alphabetic characters.", "first_name")
            is_valid = False

        return is_valid