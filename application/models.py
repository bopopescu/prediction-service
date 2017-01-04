from application import app
from application import db


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

	def __repr__(self):
		return '<User %r>' % self.name

	def is_active():
		pass
	def get_id():
		pass
	def is_anonymous():
		pass
	def is_authenticated():
		pass
