# import flask dependencies
from flask import Flask, request, make_response, jsonify
import sys
import json
from portfolio import Portfolio
from test import convert
import re
# initialize the flask app
app = Flask(__name__)
qlist = []
raw_companies = None
risk = None
portfolio = None
phone_number = None
def reset():
    global qlist, clist, risk, phone_number, portfolio
    qlist, raw_companies, risk = [], None, None
    phone_number, portfolio = None, None
# default route
@app.route('/')
def index():
    return 'Hello World!'

def compute_risk(l):
    """
    Args:
        seq[str] : sequence of user response to 13 questions
    Returns:
        str : risky-ness. either: "L", "M", "H"
    """
    assert(len(l) == 13), ("expected 13 entries but actually %d" % len(l))
    accum = 0
    one = {"A":4, "B":3, "C":2, "D":1}
    diff = {"A":1, "B":3, "C":0, "D":0}
    reg = {"A":1, "B":3, "C":3, "D":4}
    for i, val in enumerate(l):
        if i == 0:
            accum += one[val.upper()]
        elif i == 8 or i == 9:
            accum += diff[val.upper()]
        else:
            accum += reg[val.upper()]
    if accum < 21:
        return 0
    elif 21 <= accum <= 30:
        return 1
    else:
        return 2
def compute_companies(raw):
    """TODO: anish put company to ticks mapping here"""
    return raw
# create a route for webhook
@app.route('/webhook', methods=['POST'])
def webhook_post():
    global qlist, risk, raw_companies, phone_number
    data = request.get_json()
    q_type = list(data.get('queryResult').get("parameters").keys())[0]
    response = data.get('queryResult').get('queryText')
    print("Question types %s : %s" % (q_type, response))
    if q_type == "Tolerance":
        risk = response
    elif q_type == "any":
        #raw_companies = data.get('queryResult').get("parameters").values()[0]
        raw_companies = response
    elif q_type == "Response":
        response = data.get('queryResult').get("parameters").get("Response")[0]
        qlist.append(response)
    elif q_type == "Reset":
        reset()
    elif q_type == "PhoneNumber":
        print("pre append", response)
        response = response + ","
        print("post append", response)
        phone_number = "".join([s for s in re.split(';|,|\*|\n|\.|,|!|@|#|$|%|\^|&|\(|\)|-|_| ', response) if len(s) > 0])
    else:
        pass
    print("Q type", q_type)
    print("Q list", qlist)
    print("Risk factor", risk)
    print("Phone number", phone_number)
    print("Raw Companies", raw_companies)

    # check if we can calc risky
    if (len(qlist) == 13 and risk == None):
        risk = compute_risk(qlist)
        d = {"fulfillmentText" : "Hey, you have finished the questionnaire. Here is your risk: %s. Sending monthly updates to you. What's your phone number?" % risk}
        return jsonify(d)
    elif (risk is not None and phone_number is not None and raw_companies is not None):
        print("Raw Companies, if statemetn", raw_companies)
        split = [s.lower() for s in re.split(';|,|\*|\n|\.|,|!|@|#|$|%|\^|&|\(|\)|-|_| ', raw_companies + ",") if len(s) > 0]
        print("Split", split)
        companies = convert(split)
        print("Conversion of split", companies)
        portfolio = Portfolio(risk, companies)
        ret, delta = portfolio.get_market_returns()
        print(f"{ret} : {delta}")
        d = {"fulfillmentText" : f"Hey, we have added the following: {companies}. Ret: {ret}, Delta: {delta}."}
        return jsonify(d)
    return {}

# run the app
if __name__ == '__main__':
   app.run(debug=True)
