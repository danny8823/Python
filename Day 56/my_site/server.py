from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello guy</h1>"


@app.route('/personal')
def personal_page(name=None):
    return render_template("index.html", person=name)


@app.route('/testing')
def danny_page():
    return render_template("danny.html")


if __name__ == "__main__":
    app.run(debug=True)
