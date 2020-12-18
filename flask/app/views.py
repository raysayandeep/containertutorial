from app import app
import os

@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} runninh inside a docker container behind nginx!"
    
    return "Hello from flask!" 
