from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy import or_
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
mail = Mail(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key="tushies"
# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Load the views
from application import views
# from application import config

# Load the config file
app.config.from_object('config')