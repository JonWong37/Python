from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'users'
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
            
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = User(results[0])
        return user

    @classmethod   
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id =%(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id =%(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)
























# from mysqlconnection import 
# from pprint import pprint

# DATABASE = 'friends'
# class Friend:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['id']
#         self.last_name = data['id']
#         self.occupation = data['id']
#         self.created_at = data['id']
#         self.updated_at = data['id']
    
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM friends;"
#         results = connectToMySQL(DATABASE).query_db(query)