from application import app, models , mail, bcrypt
from flask import render_template, request, flash, redirect, url_for, session, jsonify, g,send_from_directory
from werkzeug import secure_filename
import requests
import os
import hashlib
from validate_email import validate_email
from flask_login import UserMixin, login_required, login_user, logout_user

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    return redirect(url_for('index'))