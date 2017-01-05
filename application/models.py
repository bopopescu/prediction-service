from application import app
from application import db
from datetime import datetime


class User(db.Model):
	__tablename__ = "users"
	id = db.Column('id', db.Integer, primary_key = True)
	name = db.Column('name', db.String(255))
	email = db.Column('email', db.String(120), unique=True)
	password = db.Column('password', db.String(120))
	registered_on = db.Column('registered_on' , db.DateTime)

	def __init__(self, name, password, email):
		self.name = name
		self.password = password
		self.email = email
		self.registered_on = str(datetime.utcnow())
		# .strftime('%Y-%m-%d %H:%M:%S')

	def __repr__(self):
		return '<User %r>' % self.name

	def is_active(self):
		return True
	def get_id(self):
		return unicode(self.id)
	def is_anonymous(self):
		return False
	def is_authenticated(self):
		return True

class PredictionType(db.Model):
	__tablename__ = "prediction_types"
	id = db.Column('id', db.Integer, primary_key = True)
	name = db.Column('name', db.String(255))

def __init__(self, name):
	self.name = name

def __repr__(self):
	return '<PredictionType %r>' % self.name

class Prediction(db.Model):
	__tablename__ = "predictions"
	id = db.Column('id', db.Integer, primary_key = True)
	game = db.Column('game', db.String(255))
	prediction_type_id = db.Column('prediction_type_id', db.Integer)
	added_on = db.Column('registered_on' , db.DateTime)
	modified_on = db.Column('registered_on' , db.DateTime)


	def __init__(self, game, prediction_type_id):
		self.game = game
		self.prediction_type_id = prediction_type_id
		self.added_on = datetime.utcnow()

	def __repr__(self):
		return '<Prediction %r>' % self.game