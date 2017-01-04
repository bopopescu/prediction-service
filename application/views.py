from application import app, models , mail, bcrypt
from flask import render_template, request, flash, redirect, url_for, session, jsonify, g,send_from_directory
from werkzeug import secure_filename
import requests
import os
import hashlib
from datetime import datetime
from validate_email import validate_email
from flask_login import UserMixin, login_required, login_user, logout_user

@app.route('/')
def index():
	return render_template('index.html')