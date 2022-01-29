from flask import Flask
from flask import request, escape


# Initialize a flask app
app = Flask(__name__)


# Decorator for intercepting requests
@app.route("/")
def index():
    celsius = str(escape(request.args.get("celsius", "")))
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """
            <form action="" method="get" autocomplete="on">
                <input type="text" name="celsius" placeholder="98.7" maxlength="50" autofocus  required>
                <input type="submit" value="convert">
            </form>
        """
        + "Fahrenheit: "
        + fahrenheit
    )


def fahrenheit_from(celsius):
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)
        return str(fahrenheit)
    except ValueError:
        return "Invalid Input: Please Enter a number"


# Main function
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)