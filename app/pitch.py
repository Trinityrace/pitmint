from flask import Flask,render;_template,url_for
#from app.forms import RegisterForm, LoginForm

app = Flask(__name__)

# app.config['SECRET_KEY']= 'covid'

pitchhs = [
    {
        'author': 'Trinity',
        'title': 'pitch post 1',
        'category': 'category',
        'content': 'first pitch content',
        'date_posted': 'feb 14, 2009'
    },
    {
        'author': 'Race',
        'title': 'pitch post 2',
        'category': 'category',
        'content': 'second pitch content',
        'date_posted': 'dec 16, 2010'
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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html',title='Register',forms=forms)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',forms=forms)

if __name__ == '__main__':
    app.run(debug=True)