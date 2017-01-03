from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify, g, send_from_directory
from werkzeug import secure_filename
from flask_sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy import or_
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
import os
import hashlib
from datetime import datetime
import requests
from flask_migrate import Migrate
from validate_email import validate_email


app = Flask(__name__)

mail = Mail(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Load the views
from application import views
# from application import config

# Load the config file
app.config.from_object('config')