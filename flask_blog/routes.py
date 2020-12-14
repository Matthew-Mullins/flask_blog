from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

posts = [
    {
        'author': 'Matthew Mullins',
        'title': 'First Post',
        'content': 'First Content',
        'date_posted': 'December 11, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Second Post',
        'content': 'Second Content',
        'date_posted': 'December 12, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Welcome {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Username or Password Incorrect', 'danger')
    return render_template('login.html', title='Login', form=form)
