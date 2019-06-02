# coding-utf8

from bottle import route, run
from bottle import post, request
from bottle import HTTPResponse
import json
import traceback


def write_to_file(d):
    with open("tmp.json", 'w') as f:
        f.write(json.dumps(d, indent=4))

@post("/do-the-work")
def do_the_work():

    try:
        write_to_file(request.json)
        return HTTPResponse(status=200)

    except Exception:
        print(traceback.print_exc())
        return HTTPResponse(status=400)

@route('/')
def index():
    return "main page."



run(host="localhost", port=8083, debug=True, reloader=True)
