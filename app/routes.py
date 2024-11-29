from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'higuchi'}
    posts = [
        { 'author': {'username':'John'},
        'body': 'Good morning from Kyoto!'},
        { 'author': {'username':'Susan'},
        'body': 'Cheese is the best!'},
        { 'author': {'username':'Asakura'},
        'body': 'Guu'}

    ]
    return render_template('index.html', title='Home', user=user,posts = posts)




