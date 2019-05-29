from flask import Flask, render_template, request, redirect, Response
import random, json, sys
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return render_template("home.html")
	
@app.route('/signUp')
def signUp():
    return render_template('signUp.html')
	
if __name__ == "__main__":
    app.run(debug=True)