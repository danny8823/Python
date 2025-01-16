from flask import Flask, render_template
import requests

app = Flask(__name__)
url = 'https://api.npoint.io/c790b4d5cab58020d391'


@app.route('/')
def home():
    blog_request = requests.get(url)
    if blog_request.status_code == 200:
        blog_data = blog_request.json()
    return render_template("index.html", blog_data=blog_data)


@app.route('/blog/<num>')
def blog_page(title, content,):
    return render_template("post.html", title=title, content=content)


if __name__ == "__main__":
    app.run(debug=True)
