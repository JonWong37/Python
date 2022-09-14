from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.doctor import Doctor
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#login page

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main')
def main():
    if 'doctor_id' not in session:
        return redirect('/')
    return render_template('main.html', recipes = Recipe.get_all())

#Register new user

@app.route('/register', methods = ['POST'])
def new():
    if not Doctor.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    if Doctor.unique_email(request.form):
        flash("Email already exists", 'taken')
        return redirect('/')
    session['first_name'] = request.form['first_name']
    user_id = Doctor.save(data)
    session['doctor_id'] = user_id
    return redirect('/loggedin')

@app.route('/loggedin')
def created():
    return redirect('/main')

# log in

@app.route('/login', methods = ['POST'])
def doctor():
    data = { 'email' : request.form['log_email']}
    user_in_db = Doctor.get_email(data)
    if not user_in_db:
        flash('Invalid E-mail address or password.', 'invalid')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['log_password']):
        flash('Invalid password.', 'invalid2')
        return redirect('/')
    session['doctor_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    return redirect('/main')

#logout

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




