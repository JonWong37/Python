from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.controllers.dojos import Dojo

# @app.route('/')
# def index():
#     ninjas = Ninja.get_all()
#     return render_template("read_all.html", ninjas = Ninja.get_all())

# Create    

@app.route('/newninja')
def create():
    dojos = Dojo.get_all()
    return render_template("newninja.html", dojos = Dojo.get_all())

@app.route('/createnew', methods = ['POST'])
def new():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/createdninja')

@app.route('/createdninja')
def created():
    return redirect('/')

    #read

@app.route('/show/<int:id>')
def show(id):
    data = {'id': id}
    ninja = Ninja.get_one(data)
    return render_template("show.html", ninja = ninja)

    # UPDATE

@app.route('/edit/<int:id>')
def edit(id):
    data = {'id': id}
    return render_template('edit.html', ninja = Ninja.get_one(data))

@app.route('/update/ninja', methods = ['POST'])
def updateninja():
    Ninja.update(request.form)
    return redirect(f"/show/{request.form['id']}")


#thanos them

@app.route('/delete/<int:id>')
def thanos(id):
    Ninja.delete({'id':id })
    return redirect('/')