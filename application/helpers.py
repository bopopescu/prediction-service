import requests
from application import mail
from flask_mail import Message

def sendMail(subject, sndr,  body, email, email_type=False):
	try:
		msg = Message(subject, sender=sndr,recipients=[email])
		if not email_type:
			msg.body = body
		else:
			msg.html = render_template("email.html", body=body)
		mail.send(msg)
		return 'Mail sent!'
	except Exception, e:
		return(str(e))

def sendSMS(recipient, body):
	try:
		data = {'username': config.SMS_API_USERNAME, 'password': config.SMS_API_PASSWORD, 'recipient': recipient, 'sender':'tushworks', 'message': body}
		r = requests.get(config.SMS_API_URL, params = data)
		return r.json
	except Exception as e:
		return(str(e))
