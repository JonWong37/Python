
from flask_app import app
from flask_app.controllers.doctors import Doctor
from flask_app.controllers.recipes import Recipe




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.