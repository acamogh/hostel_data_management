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
        session['logged_in'] = True
        return send_file('static/templates/data_entry.html')
    error = "Invalid usernae or password"
    return render_template('main.html',error=error)



@app.route("/show_data")
def show_data():
    return send_file('static/templates/show_data.html')

@app.route("/student_datails", methods=['POST'])
def student_datails():
    name=request.form['student_name']
    number=request.form['register_number']
    coll_name=request.form['college_name']
    town=request.form['home_town']

    print name,number,coll_name,town
    return ('',203)





@app.route("/logout")
def logout():
    session.pop('logged_in',False)
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(debug=True)