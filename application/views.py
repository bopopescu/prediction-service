from application import app
from application import models

@app.route('/')
def index():
	return "Hello world"