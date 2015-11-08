from flask import send_file, g, session, Flask,render_template, request, jsonify, make_response, flash, redirect, url_for
from functools import wraps

import os, json
app = Flask(__name__)

app.secret_key = "1st_Hostel_data_managament !!"

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


@app.route("/")
def hello():
    return render_template('main.html')

@app.route("/login", methods=['GET','post'])
def login_details():
    error=None
    username = request.form['username']
    password = request.form['password']
    if username == 'qw' and password == 'qw':
        return send_file('static/templates/admin.html')
    error = "Invalid usernae or password"
    return render_template('main.html',error=error)

if __name__ == "__main__":
    app.run(debug=True)