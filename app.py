from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    "Show homepage"
    return render_template('index.html', index=index)

@app.route('/sign-in')
def sign_in():
    "sign in page"
    return render_template('sign_in.html', sigh_in=sign_in)

@app.route('/sign-up')
def sign_up():
    "sign_up page"
    return render_template('sign_up.html', sigh_up=sign_up)

@app.route('/profile')
def profile():
    return render_template('profile.html', profile=profile)

@app.route('/about')
def about():
    return render_template('about.html', about=about)

if __name__ == '__main__':
    app.run(debug=True)

    
