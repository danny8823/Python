from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"],
                    post["subtitle"], post["body"], post["image_url"])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/samplepost')
def samplepost():
    return render_template("samplepost.html")


@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
