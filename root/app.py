from flask import Flask

app = Flask(__name__)



@app.route('/<name>')
def hello(name):
    return 'Hello, {0}'.format(name)


@app.route('/')
def index():
    return 'Its works!'