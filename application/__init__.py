from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import redis

app = Flask(__name__)

app.config['SECRET_KEY'] = 'eeabd520b0cb29de98c98f740ee13b0a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

r = redis.StrictRedis(host='localhost', port=6379, db=0)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'



from application import routes