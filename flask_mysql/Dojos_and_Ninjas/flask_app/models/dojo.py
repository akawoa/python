# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database for all Dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    # Class method to look up a single dojo's ninjas
    @classmethod
    def select_dojo(cls, data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos on dojos.id = ninjas.dojo_id WHERE dojo_id=%(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
                # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        # resultObject = cls(results[0])
        # print(resultObject)
        return ninjas


        # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(dname)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )
    
            # class method to save our friend to the database
