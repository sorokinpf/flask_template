from app import app
from flask import render_template

@app.route('/')
def template():
   return render_template('home.html')

@app.route('/hello')
def home():
   return "hello world!"
