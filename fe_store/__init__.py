from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "3756Hjj_09i#yysnu&uuy^%6788"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fe_store.db'
db = SQLAlchemy(app)

from fe_store import routes