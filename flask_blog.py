from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b39623ed00fa60495b588c0155bd8948'

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)