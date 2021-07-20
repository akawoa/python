# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the friend table from our database
class Survey:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.", "name")
            is_valid = False
        if len(survey['location']) == 0:
            flash("Location must be at least 3 characters.", "location")
            is_valid = False
        if len(survey['language']) == 0:
            flash("Language must be at least 3 characters.", "language")
            is_valid = False
        return is_valid


    # Now we use class methods to query our database for all Dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo_survey;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        # Create an empty list to append our instances of friends
        surveys = []
        # Iterate over the db results and create instances of friends with cls.
        for survey in results:
            surveys.append( cls(survey) )
        return surveys


        # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojo_survey ( name, location, language, created_at, updated_at ) VALUES ( %(name)s, %(location)s, %(language)s, current_timestamp(), current_timestamp());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey_schema').query_db( query, data )
    
            # class method to save our friend to the database
