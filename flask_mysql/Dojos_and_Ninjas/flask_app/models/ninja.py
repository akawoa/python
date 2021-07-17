# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dojo_id = data['dojo_id']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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

    # Class method to look up a single user
    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL('users').query_db(query, data)
        resultObject = cls(results[0])
        print(resultObject)
        return resultObject


        # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age , image , dojo_id, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(age)s , %(image)s , %(dojo_id)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )
    
            # class method to save our friend to the database
    @classmethod
    def edit(cls, data ):
        query = "UPDATE users SET first_name = %(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=now() WHERE id = %(id)s;"
        print(query)
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )
    
    #Class method to delete a single user
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM users WHERE id=%(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )