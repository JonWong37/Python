from itertools import count
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)    
app.secret_key = 'chicken nuggets'


@app.route('/')         
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 0
    return render_template("index.html")

@app.route('/up')
def up():
    session['count'] += 1
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/down')
def down():
    session['count'] -= 1
    return redirect('/')

@app.route('/input', methods = ['POST'])
def input():
    print(type(request.form['key']))
    session['key'] = request.form['key']
    if int(session['key']) >= 0:
        session['count'] += int(session['key'])
    # elif int(session['key']) < 0 :
    #     session['count'] += -abs(int(session['key']))
    else:
        session['count'] += int(session['key'])
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.