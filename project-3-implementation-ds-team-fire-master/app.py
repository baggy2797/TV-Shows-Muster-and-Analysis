from flask import Flask, request, Response, jsonify, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
import pandas as pd
import config
import os
import datetime
import re

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

class SentimentForm(Form):
    min_score = StringField('min_score', validators=[DataRequired()])
    max_score = StringField('max_score', validators=[DataRequired()])
    num_reviews = StringField('num_reviews', validators=[DataRequired()])

class RatingsForm(Form):
    min_score = StringField('min_score', validators=[DataRequired()])

def format(message, status):
    return jsonify({"message": message, "status": status})

@app.route('/', methods=['GET'])
def hello():
	return redirect(url_for('sentiment_viz'))

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment_viz():
    form = SentimentForm()
    if form.validate_on_submit():
        min_score = str(form.min_score.data)
        max_score = str(form.max_score.data)
        num_reviews = str(form.num_reviews.data)
        info = return_reviews_between_sentiments(min_score, max_score, num_reviews)
        colnames = ['Title', 'Review', 'Score']
        return render_template('sentiment.html', form=form, colnames=colnames, records=info, showdetails=True)
    return render_template('sentiment.html', form=form, showdetails=False)

@app.route('/rating', methods=['GET', 'POST'])
def ratings_viz():
    form = RatingsForm()
    if form.validate_on_submit():
        min_score = str(form.min_score.data)
        info = return_shows_above_rating(min_score)
        colnames = ['Title', 'Rating']
        return render_template('rating.html', form=form, colnames=colnames, records=info, showdetails=True)
    return render_template('rating.html', form=form, showdetails=False)

def return_shows_above_rating(threshold):
    df = pd.read_csv('ratings_viz.csv')
    rated_shows = df[df['imdbRating'] > float(threshold)].sort_values(by=['imdbRating'], ascending=False)
    display_info = []
    for idx, row in rated_shows.iterrows():
    	info = {}
    	info['Title'] = row['Title']
    	info['Rating'] = row['imdbRating']
    	display_info.append(info)
    return display_info

def return_reviews_between_sentiments(min_score, max_score, num_reviews):
    df = pd.read_csv('sentiment_viz.csv')
    min_score = float(min_score)
    max_score = float(max_score)
    good_shows = df[df['sentiment_score'].between(min_score, max_score)]
    display_df = good_shows.sample(n=int(num_reviews), random_state=69)
    display_info = []
    for idx, row in display_df.iterrows():
        info = {}
        info['Title'] = row['Title']
        info['Review'] = row['Review']
        info['Score'] = row['sentiment_score']
        display_info.append(info)
    return display_info

if __name__ == '__main__':
    app.run()