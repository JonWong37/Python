from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/')         
def hello_people():
    
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("index.html", users = users)

#Playground


#     <!-- <h1>Hello Flask!</h1>
#     <h3>My Flask Template</h3>
# <p>Phrase: {{ phrase }}</p>
# <p>Times: {{ times }}</p>

# {% for x in range(0,times): %}
#     <p>{{ phrase }}</p>
# {% endfor %}

# {% if phrase == "hello" %}
#     <p>The phrase says hello</p>
# {% endif %} -->


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.