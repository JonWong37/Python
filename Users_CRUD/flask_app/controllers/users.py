from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template("read_all.html", users = User.get_all())

# Create    

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/createnew', methods = ['POST'])
def new():
    User.save(request.form)
    return redirect('/createduser')

@app.route('/createduser')
def created():
    return redirect('/')

    #read

@app.route('/show/<int:id>')
def show(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template("show.html", user = user)

    # UPDATE

@app.route('/edit/<int:id>')
def edit(id):
    data = {'id': id}
    return render_template('edit.html', user = User.get_one(data))

@app.route('/update/user', methods = ['POST'])
def updateuser():
    User.update(request.form)
    return redirect(f"/show/{request.form['id']}")


#thanos them

@app.route('/delete/<int:id>')
def thanos(id):
    User.delete({'id':id })
    return redirect('/')