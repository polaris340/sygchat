import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, redirect
import pusher




#create app
app = Flask(__name__)

def create_pusher():
	p=pusher.Pusher(
		app_id = '79026',
		key = '5c4043a6d9b4d7f1da8d',
		secret='87d7aa6bcf3aed63b7e7'
	)
	return p

def get_pusher():
	if not hasattr(g,'pusher'):
		g.pusher = create_pusher()
	return g.pusher
	

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
	return 'login'

@app.route('/logout')
def logout():
	return 'logout'

@app.route('/pusher_test')
def pusher_test():
	get_pusher()['channel'].trigger('my_event',{'message':'hello world'})
	return 'hello world'


#################### run server#######################################################
if __name__ == '__main__' :
	app.debug = True
	app.run(host='0.0.0.0', port=5001)
