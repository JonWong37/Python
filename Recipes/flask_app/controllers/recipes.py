from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.doctor import Doctor
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



# New recipe

@app.route('/newrecipe')
def newrrecipe():
    if 'doctor_id' not in session:
        return redirect('/')
    return render_template('newrecipe.html')

# Saves new recipe

@app.route('/createnew', methods = ['POST'])
def createnewrecipe():
    print(request.form)
    if not Recipe.validate(request.form):
        return redirect('/newrecipe')
    Recipe.save(request.form)
    return redirect('/newrec')

@app.route('/newrec')
def savedrec():
    recipes = Recipe.get_all()
    return redirect('/main')

# SHOW RECIPE CARD / ID

@app.route('/show/<int:id>')
def show(id):
    if 'doctor_id' not in session:
        return redirect('/')
    data = {'id': id}
    recipe = Recipe.get_one(data)
    return render_template("show.html", recipe = recipe)

# UPDATE RECIPE 

@app.route('/update/<int:id>')
def edit(id):
    if 'doctor_id' not in session:
        return redirect('/')
    data = {'id': id}
    recipe = Recipe.get_one(data)
    return render_template('update.html', recipe = recipe)

#SAVING RECIPE UDATE

@app.route('/update/recipe', methods = ['POST'])
def updaterecipe():
    if not Recipe.validate(request.form):
        return redirect(f"/update/{request.form['id']}")
    Recipe.update(request.form)
    return redirect(f"/show/{request.form['id']}")

#thanos them

@app.route('/delete/<int:id>')
def thanositem(id):
    Recipe.delete({'id':id })
    return redirect('/main')

