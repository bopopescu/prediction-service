from application import app, models , mail, db, bcrypt, login_manager
from flask import render_template, request, flash, redirect, url_for, session, jsonify, g,send_from_directory, make_response
from werkzeug import secure_filename
import requests
import os
import hashlib
from validate_email import validate_email
from flask_login import UserMixin, login_required, login_user, logout_user
import csv
import io

@app.route('/')
def index():
	return render_template('index.html')

@login_manager.user_loader
def load_user(id):
	# pass
    return models.User.query.get(int(id))

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

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
	return render_template("dashboard.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_prediction():
    if request.method == "POST":
        file = request.files['file']
        if not file:
            return "No file"
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)

        for row in csv_input:
            prediction = models.Prediction(game=row[0], prediction_type_id=row[1])
            db.session.add(prediction)
            db.session.commit()
        flash('CSV uploaded', 'success')
    return render_template("upload.html")

@app.route('/predictions', methods=['GET'])
@login_required
def pediction_list():
    return render_template("prediction_list.html")

@app.route('/subscription', methods=['GET', 'POST'])
@login_required
def subscription_page():
    pass

@app.route('/predictions', methods=['GET', 'POST'])
@login_required
def payment():
    pass
