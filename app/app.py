from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
import sys
import secrets

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html', year=datetime.now().year)

@app.route('/connect')
def connect():
    return render_template('connect.html', year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about-us.html', year=datetime.now().year)

@app.route('/birth')
def birth():
    return render_template('birth.html', year=datetime.now().year)

@app.route('/postpartum')
def postpartum():
    return render_template('postpartum.html', year=datetime.now().year)

@app.route('/doulas')
def doulas():
    return render_template('meet-doulas.html', year=datetime.now().year)

@app.route('/rental')
def rental():
    return render_template('rentals.html', year=datetime.now().year)

@app.route('/resources')
def resources():
    return render_template('resources.html', year=datetime.now().year)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
