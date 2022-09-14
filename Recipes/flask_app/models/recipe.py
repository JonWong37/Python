from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request, redirect
import re


DATABASE = 'doctors_recipes'
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.food_name = data['food_name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under = data['under']
        if 'first_name' in data :
            self.first_name = data['first_name']
        self.date = data['date']
        self.doctor_id = data['doctor_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #CREATE / SAVE

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (food_name, description, instructions, under, date, doctor_id) VALUES (%(food_name)s, %(description)s, %(instructions)s, %(under)s, %(date)s, %(doctor_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # READ ALL

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN doctors ON recipes.doctor_id = doctors.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    # GET ONE RECIPE TO DISPLAY OWNER NAME

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN doctors ON recipes.doctor_id = doctors.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        recipes = Recipe(results[0])
        return recipes
    
    # READ ONE SPECIC DOCTOR

    @classmethod
    def get_one_doctor(cls,data):
        query = "SELECT * FROM recipes LEFT JOIN doctors ON recipes.doctor_id = doctors.id;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        recipes = Recipe(results[0])
        return recipes
    

# Update / Delete

    @classmethod   
    def update(cls, data):
        query = "UPDATE recipes SET food_name = %(food_name)s, description = %(description)s, instructions = %(instructions)s WHERE id = %(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

    # Validation

    @staticmethod
    def validate(recipe):
        is_valid = True
        if len(recipe['food_name']) < 2:
            flash("Food name needs to be at least 3 characters.", 'food_name')
            is_valid = False
        if len(recipe['description']) < 1:
            flash("Instructions cannot be blank", 'description')
            is_valid = False
        if len(recipe['instructions']) < 1:
            flash("Instructions cannot be blank", 'instructions')
            is_valid = False
        if 'under' not in recipe:
            flash(" Please select one", 'under')
            is_valid = False
        if len(recipe['date']) < 1:
            flash("Please select a date", 'date')
            is_valid = False
        return is_valid
