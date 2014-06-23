import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, redirect
import pusher




#create app
app = Flask(__name__)
app.secret_key = 'sdfjaiAWFa3092%@'

def get_pusher():
	if not hasattr(g,'pusher'):
		g.pusher = pusher.Pusher(
			app_id = '79029',
			key='1d81fdd2355a7d0819e3',
			secret='3f54501fe2f593d2605e'
		)
	return g.pusher




@app.route('/')
def index():
	if 'username' in session:
		return render_template('index.html')
	else:
		return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
	session['username'] = request.form['username']
	return redirect(url_for('index'))

@app.route('/logout')
def logout():
	return 'logout'
	
@app.route('/chat')
def chat():
	return render_template('chat.html')

@app.route('/send', methods = ['GET','POST'])
def send():
	get_pusher()['test_channel'].trigger('my_event', {'username':session['username'],'message': request.args.get('message','')})
	return ''



#################### run server#######################################################
if __name__ == '__main__' :
	app.debug = True
	app.run(host='0.0.0.0', port=5001)

