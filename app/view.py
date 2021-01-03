from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Vlad'
    return render_template('index.html', n=name)

