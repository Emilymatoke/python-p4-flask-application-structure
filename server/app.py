#!/usr/bin/env python3

from flask import Flask

#Flask class requires only name as the primary module
app = Flask(__name__)

#app.route -url and code association to process requests
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
    