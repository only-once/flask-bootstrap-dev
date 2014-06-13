from flask import Flask,request,jsonify,redirect,url_for
from flask import render_template


app = Flask(__name__)

app.debug = True

@app.route("/")
def home():
    return render_template('pages/home.html')

# Catch all :)
cool404s = [
		'WR2FvrU-NIM',
		'wNVCJj642n4',
		'dn_CjkNtl6s',
		'f5IRI4oHKNU',
		]
import random
@app.route('/<path:path>')
def catch_all(path):
	return render_template('pages/404.html', video=random.choice(cool404s))
