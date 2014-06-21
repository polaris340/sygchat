import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, redirect



#create app
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')



#################### run server#######################################################
if __name__ == '__main__' :
	app.run(host='0.0.0.0', port=5001)