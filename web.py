from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Ivan! updating direct to master 12-dic-2018'
