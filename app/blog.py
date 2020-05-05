from flask import Flask,render_template,url_for
# from app.forms import RegisterForm, LoginForm

app = Flask(__name__)

# app.config['SECRET_KEY']= 'covid'

pitchhs = [
    {
        'author': 'Trinity',
        'title': 'blog post 1',
        'content': 'first post contant',
        'content': 'first post content',
        'date_posted': 'feb 14, 2019'
    },
    {
        'author': 'Race',
        'title': 'blog post 2',
        'content': 'second post contant',
        'content': 'second post content',
        'date_posted': 'feb 16, 2019'
    }
    ]


@app.route('/')
# def hello():
#     return '<h1>Hello, Covid!</h1>'

@app.route("/home")
def home():
    return render_template('index.html',pitchs=pitchhs)

@app.route("/about")
def about():
    return render_template('about.html',title=about)
if __name__ == '__main__':
    app.run(debug=True)