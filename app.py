# import flask dependencies
from flask import Flask, request, make_response, jsonify
import sys
import json
# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

def f(l):
    """
    Args:
        seq[str] : sequence of user response to 13 questions
    Returns:
        str : risky-ness. either: "L", "M", "H"
    """
    assert(len(l) == 13), f"expecting 13 entries, but actual: {len(l)}"
    accum = 0
    one = {"a":4, "b":3, "c":2, "d":1}
    diff = {"a":1, "b":3, "c":0, "d":0}
    reg = {"a":1, "b":3, "c":3, "d":4}
    for i, val in enumerate(l):
        if i == 0:
            accum += one[val]
        elif i == 8 or i == 9:
            accum += diff[val]
        else:
            accum += reg[val]
    if accum < 21:
        return "L"
    elif 21 <= accum <= 30:
        return "M"
    else:
        return "H"

# create a route for webhook
@app.route('/webhook', methods=['POST'])
def webhook_post():
    data = request.get_json()
    action = data.get('queryResult')
    print data
    return {}

# run the app
if __name__ == '__main__':
   app.run(debug=True)
