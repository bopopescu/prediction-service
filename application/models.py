from application import app
from application import db
from datetime import datetime


class User(db.Model):
	__tablename__ = "users"
	id = db.Column('id', db.Integer, primary_key = True)
	name = db.Column('name', db.String(255))
	email = db.Column('email', db.String(120), unique=True)
	password = db.Column('password', db.String(120))

	def __init__(self, name, email, password):
		self.name = name
		self.password = password
		self.email = email
		self.registered_on = datetime.utcnow()

	def __repr__(self):
		return '<User %r>' % self.name

	def is_active():
		return True
	def get_id(id):
		return unicode(self.id)
	def is_anonymous():
		return False
	def is_authenticated():
		return True
