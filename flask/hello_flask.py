from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# Used secrets.token_hex() to generate this token
app.config['SECRET_KEY'] = '87e5bef19cad3e5b24b888d25653d79a'

posts = [
    {
        'author': 'Arun Narayanan',
        'title': 'Beginning Python',
        'content': 'My first content',
        'date_posted': 'Dec 30, 2020'
    },
    {
        'author': 'Tom Hanks',
        'title': 'GTD',
        'content': 'GTD is cool',
        'date_posted': 'Dec 28, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', all_posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='My Title')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}.', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Please check username & password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
