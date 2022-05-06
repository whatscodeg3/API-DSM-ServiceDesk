from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bcda6317f670c5:56674bf3@us-cdbr-east-05.cleardb.net/heroku_041f3b642f4313b'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(contacts)
