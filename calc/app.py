from operations import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def do_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)

    return result


@app.route('/sub')
def do_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)

    return result

@app.route('/mult')
def do_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)

    return result

@app.route('/div')
def do_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)

    return result