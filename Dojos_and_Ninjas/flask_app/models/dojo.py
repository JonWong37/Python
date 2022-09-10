from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

DATABASE = 'dojos_ninjas'
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
            
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        return dojo

    @classmethod   
    def update(cls, data):
        query = "UPDATE dojos SET name = %(name)s, last_name = %(last_name)s, email = %(email)s WHERE id =%(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos WHERE id =%(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

#this is trying to combine ninjas and dojos

    @classmethod
    def get_one_with_ninja(cls, data):
        # TODO write a join sql query to get a dojo and all its ninjas
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # TODO the query will be a list of dictionaries. Each dictionary will contain all the attributes of the dojo and one of the dojo's ninjas.
        dojo = Dojo(results[0])
        # TODO create an instance of the dojo class that will have the ninjas attribute. The attribute is a list of all that dojo's ninjas
        # TODO loop over the list of dictionaries returned from the database.
        for result in results :
        # TODO create a dictionary to hold and format the ninja's data from each dictionary.
            temp_ninja = {
                "id" : result['ninjas.id'],
                "first_name" : result['first_name'],
                "last_name" : result['last_name'],
                "age" : result['age'],
                "created_at" : result['created_at'],
                "updated_at" : result['updated_at']
            }
        # TODO append `ninjas.`to the attributes where needed:
            # TODO once the dictionary is created for each ninjas, append it to the ninjas attribute list. Inside the append method, convert the dictionary created in the previous step to an instance of the ninja class.
            dojo.ninjas.append(Ninja(temp_ninja))
    # TODO finally, return the dojo created above. It will contain the ninjas attribute created in the for loop above.
        return dojo





















# from mysqlconnection import 
# from pprint import pprint

# DATABASE = 'friends'
# class Friend:
#     def __init__(self, data):
#         self.id = data['id']
#         self.name = data['id']
#         self.last_name = data['id']
#         self.occupation = data['id']
#         self.created_at = data['id']
#         self.updated_at = data['id']
    
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM friends;"
#         results = connectToMySQL(DATABASE).query_db(query)