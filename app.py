import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, redirect
import pusher




#create app
app = Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
	return 'login'

@app.route('/logout')
def logout():
	return 'logout'



#################### run server#######################################################
if __name__ == '__main__' :
	app.debug = True

	p=pusher.Pusher(
		app_id = '79026',
		key = '5c4043a6d9b4d7f1da8d',
		secret='87d7aa6bcf3aed63b7e7'
	)
	get_pusher()['channel'].trigger('my_event',{'message':'hello world'})


	app.run(host='0.0.0.0', port=5001)

