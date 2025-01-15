from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/")
def hello_world():
    return "<h1 style = 'text-align: center'>Hello, World!</h1>"\
        "<p>My paragraph</p>"\
        "<img src = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnR1MzBxeXJ2Y2Rqemp4cGQweWNyaGdkeGEzamoyc2Z0d29xbnc2ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HJZblxmxHb7CbZtmNy/giphy.gif' alt = 'cat' width=200/>"\
        "<p>The other paragraph</p>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there, {name}, you are {number}!"


if __name__ == "__main__":
    app.run(debug=True)
