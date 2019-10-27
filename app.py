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
