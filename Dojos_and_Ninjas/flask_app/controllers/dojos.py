from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def indexdj():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = Dojo.get_all())

# Create    

# @app.route('/create')
# def create():
#     return render_template("create.html")

@app.route('/createdj', methods = ['POST'])
def newdj():
    Dojo.save(request.form)
    return redirect('/createddojo')

@app.route('/createddojo')
def createddj():
    return redirect('/')

    #read

@app.route('/dojos/<int:id>')
def showdj(id):
    data = {'id': id}
    dojo = Dojo.get_one_with_ninja(data)
    return render_template("show.html", dojo = dojo)

    # UPDATE

# @app.route('/edit/<int:id>')
# def edit(id):
#     data = {'id': id}
#     return render_template('edit.html', dojo = Dojo.get_one(data))

# @app.route('/update/dojo', methods = ['POST'])
# def updatedojo():
#     Dojo.update(request.form)
#     return redirect(f"/show/{request.form['id']}")


#thanos them

# @app.route('/delete/<int:id>')
# def thanos(id):
#     Dojo.delete({'id':id })
#     return redirect('/')