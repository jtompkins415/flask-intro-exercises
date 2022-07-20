from operations import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def do_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = add(a,b)

    return str(total)


@app.route('/sub')
def do_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = sub(a,b)

    return str(total)

@app.route('/mult')
def do_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)

    return str(result)

@app.route('/div')
def do_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)

    return str(result)


#PART TWO

math_functions = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/operations/<funct>')
def do_math(funct):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = math_functions[funct](a,b)

    return str(result)