from flask import Flask, render_template, request, redirect
from jinja2 import Environment, FileSystemLoader, Template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['WEEK00_TEAM7']
collection = db['A']
collection2 = db['B']
collection3 = db['C']

@app.route('/')
def loginRender():
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def registerRender():
    return render_template("register.html")

@app.route('/main', methods=['POST'])
def mainRender():
    return render_template("main.html")

@app.route('/login' , methods=['POST'])
def login():
    return 'hello'

if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)