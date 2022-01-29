from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/<celsius>")
def fahrenheit_from(celsius):
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)
        return str(fahrenheit)
    except ValueError:
        return "Invalid Input: Please Enter a number"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)