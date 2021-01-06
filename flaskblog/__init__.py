from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Used secrets.token_hex() to generate this token
app.config['SECRET_KEY'] = '87e5bef19cad3e5b24b888d25653d79a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
