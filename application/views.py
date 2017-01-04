from application import app, models , mail, db, bcrypt
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
    user = models.User(request.form['name'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form['email']
    password = request.form['password']
    registered_user = models.User.query.filter_by(email=email,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))