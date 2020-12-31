from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello():
    return render_template('home.html', all_posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='My Title')


if __name__ == '__main__':
    app.run(debug=True)
