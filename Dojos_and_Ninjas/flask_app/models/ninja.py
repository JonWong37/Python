from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_ninjas'
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
            
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        ninja = Ninja(results[0])
        return ninja

    @classmethod   
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id =%(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id =%(id)s; "
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