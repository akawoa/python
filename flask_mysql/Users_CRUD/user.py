# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def test(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL('users').query_db(query, data)
        resultObject = cls(results[0])
        print(resultObject)
        return resultObject

    # Class method to look up a single user
    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM users WHERE id=%(user_id)d;"
        print("Query")
        print(query)
        data = {
            "user_id": user_id
        }
        print("Data:")
        print(data)
        print("Data[user_id]")
        print(data["user_id"])
        results = connectToMySQL('mydb').query_db(query)
        # This is just an example of what you could do with the results.
        print("Results")
        print(results)
        if len(results) > 0:
            return results[0]
        else:
            return False

        # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )