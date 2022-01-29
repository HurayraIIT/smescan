from flask import Flask
from flask import request, escape
from smescan import *


app = Flask(__name__)


@app.route("/")
def index():
    
    URL = str(escape(request.args.get("website", "")))
    USERNAME = str(escape(request.args.get("email", "")))
    PASSWORD = str(escape(request.args.get("password", "")))
    
    if URL and USERNAME and PASSWORD:
        OUTPUT = RunSmeScan(URL, USERNAME, PASSWORD)
    else:
        OUTPUT = "empty"
    
    
    return (
        """
        <form action="" method="get" autocomplete="on">
        
            <p>Select Website:</p>
            
            <input type="radio" id="testing" name="website" value="https://testing.smevai.com" checked>
            <label for="testing">Testing</label>
            <input type="radio" id="app" name="website" value="https://app.smevai.com">
            <label for="app">App</label><br> <br>
            
            
            <p>User Email:</p>
            <input type="email" name="email" value="wpdabh+year22ta1@gmail.com" required> <br><br>
            
            <p>User Password:</p>
            <input type="text" name="password" value="pass1234" required> <br><br>
            
            <input type="submit" value="send">
        </form>
        """
        + OUTPUT
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    