from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1, 10)
    current_year = datetime.now().year
    print(current_year)
    return render_template('index.html', num=random_num, current_year=current_year, name='Danny')


@app.route('/guess/<some_name>')
def guess(some_name):
    name_res = requests.get(f'https://api.agify.io?name={some_name}')
    gender_res = requests.get(f'http://api.genderize.io?name={some_name}')
    if gender_res.status_code == 200:
        gender_data = gender_res.json()
    if name_res.status_code == 200:
        name_data = name_res.json()
    current_year = datetime.now().year
    return render_template('guess.html', current_year=current_year, name='Danny', name_data=name_data, gender_data=gender_data)


@app.route('/blog/<num>')
def blog_page(num):
    print(num)
    current_year = datetime.now().year
    blog_res = requests.get('https://api.npoint.io/9e6352cca26463c5e8b4')
    if blog_res.status_code == 200:
        blog_data = blog_res.json()
    return render_template('blog.html', current_year=current_year, name='Danny', blog_data=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
