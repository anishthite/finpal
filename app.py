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
def webhook():
    print("webhook");sys.stdout.flush()
    print(request.json)

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    print('hi')
    # text = req.get('queryResult')
    #action = req.get('queryAction').get('action')

    return 'yes'

# run the app
if __name__ == '__main__':
   app.run()
