from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, IPAddress
import csv

coffee_rating_choices = [('☕'), ('☕☕'), ('☕☕☕'), ('☕☕☕☕'), ('☕☕☕☕☕')]
wifi_rating_choices = [('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')]
power_rating_choices = [('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')]


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[
                       DataRequired(message="Cafe name is required")])
    location = StringField(
        label='Cafe Location on Google Maps(URL)', validators=[IPAddress()])
    open_time = StringField(label='Opening Time e.g. 8AM',
                            validators=[DataRequired(message="Open Time is required")])
    close_time = StringField(
        label='Closing Time e.g. 11PM', validators=[DataRequired(message="Close Time is Required")])
    coffee_rating = SelectField(
        label='Coffee Rating', choices=coffee_rating_choices, validators=[DataRequired(message="pick one")])
    wifi_rating = SelectField(
        label='WIFI Power Rating', choices=wifi_rating_choices, validators=[DataRequired(message="pick one")])
    power_rating = SelectField(
        label='Power Outlet Rating', choices=power_rating_choices, validators=[DataRequired(message="pick one")]
    )
    submit = SubmitField(label='Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('/Users/danny714/Desktop/Python/Day 62/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
