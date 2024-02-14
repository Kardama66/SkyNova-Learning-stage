from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Radziu'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Steve'},
            'body': 'Testing Everything'
        },
        {
            'author': {'username': 'Rajesh'},
            'body': 'I would like to eat apple'
        }
    ]
    return render_template('index.html', title='Ziomo', user=user, posts=posts)#returning html template from file index.html


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() #Taking class from other file (imported above)
    if form.validate_on_submit(): #Submiting
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index')) #Redirecting to index
    return render_template('login.html', title='Sign In', form=form)