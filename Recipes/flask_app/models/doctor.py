from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request, redirect
from flask_app.models.recipe import Recipe
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



DATABASE = 'doctors_recipes'
class Doctor:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.recipes = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO doctors_recipes.doctors (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM doctors;"
        results = connectToMySQL(DATABASE).query_db(query)
        doctors = []
        for doctor in results:
            doctors.append( cls(doctor) )
        return doctors

    # Get Email

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM doctors_recipes.doctors WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        doctor = Doctor(results[0])
        return doctor

    # unique email checker 

    @classmethod
    def unique_email(cls,data):
        query = "SELECT * FROM doctors_recipes.doctors WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(request.form['email'], results)
        return len(results) == 1

    # GET ONE DOCTOR

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM doctor WHERE first_name = %(first_name)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        doctor = Doctor(results[0])
        return doctor

    # Validation

    @staticmethod
    def validate(doctor):
        is_valid = True
        if len(doctor['first_name']) < 2:
            flash("First name needs to be at least 2 characters.", 'first_name')
            is_valid = False
        if len(doctor['last_name']) < 2:
            flash("Last name needs to be atleast 2 characters", 'last_name')
            is_valid = False
        if not EMAIL_REGEX.match(doctor['email']):
            flash("Invalid email address!!", 'email')
            is_valid = False
        if len(doctor['password']) == 0 or len(doctor['password']) < 3 :    
            flash("Please enter a password", 'password')
            is_valid = False
        if doctor['password'] != doctor['password_confirm']:
            flash("Passwords do not match", 'password_confirm')
            is_valid = False
        return is_valid

    @classmethod
    def get_one_with_recipe(cls, data):
        query = "SELECT * FROM doctors LEFT JOIN recipes ON doctors.id = recipes.doctor_id WHERE doctors.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        doctor = Doctor(results[0])
        for result in results :
            temp_recipe = {
                "id" : result['recipes.id'],
                "first_name" : result['first_name'],
                "last_name" : result['last_name'],
                "created_at" : result['created_at'],
                "updated_at" : result['updated_at']
            }
            doctor.recipes.append(Recipe(temp_recipe))
        return doctor

