from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route('/login')
def login():
    pass

@app.route('/register')
def register():
    pass

if __name__ == "__main__":
    app.run(debug=True)