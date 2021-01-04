from app import app
from flask import render_template


@app.route('/')
def index():
    '''
    Main page "/"
    '''

    name = 'Vlad'
    return render_template('index.html', n=name)

