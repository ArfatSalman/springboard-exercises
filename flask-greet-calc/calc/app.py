from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def do_add():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)


@app.route('/sub')
def do_sub():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)


@app.route('/mult')
def do_mult():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)


@app.route('/div')
def do_div():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)


operators = {"add": add, "sub": sub,
             "mult": mult, "div": div}


@app.route('/math/<opp>')
def do_math(opp):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[opp](a, b)
    return str(result)
