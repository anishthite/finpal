import requests
import json
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


company = get_symbol("MSFT")

print(company)


stringdic = {
'blackrock' : 'BLK',
'att' : 'T',
'apple' : 'AAPL',
'microsoft' : 'MSFT',
'google' : 'GOOG',
'facebook' : 'FB',
'nike' : 'NKE',
'southwest' : 'LUV'
}


def convert(tokenized_string_list):
    actual_list = []
    for company in tokenized_string_list:
        if company.lower() in stringdic:
            actual_list.append(stringdic[company.lower()])
    return actual_list






# def convertstock(stocks, proporitons):
#     string = ''
#     positioncounter = 0
#     for stock in stocks:
#         ''.join(string,stock,'~')


# portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={
#     'positions' : 'BLK~50|SNP500~50',
#     'outputFormat': 'json',
#     'calculateExposures': 'true',
#     'calculatePerformance':'true',
#     'prettifyJson':'true'
# })
# portfolioAnalysisRequest.text # get in text string format
# portfolioAnalysisRequest.json() # get as json object
# y = json.loads(portfolioAnalysisRequest.text)
# #print(y)

# y = y['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['latestPerf'].keys()
# #['riskData']['totalRisk']#['weightedAveragePerformance']
# #  :  3,
# #  :  1.75,
# # rnrRatingY3 :  2.5,
# # rnrRatingY5 :  3.25,
# #  :  3.99,
# # rnrRiskAdjustedReturnY10 :  3.395,
# # rnrRiskAdjustedReturnY3 :  3.525,
# # rnrRiskAdjustedReturnY5 :  3.58,
# # rnrRiskRatingOverall :  1.75,
# # rnrRiskRatingY10 :  1.5,
# # rnrRiskRatingY3 :  1.75,
# # rnrRiskRatingY5 :  2,
# #  :  0.6625,
# # rnrRiskScoreY10 :  0.4775,
# # rnrRiskScoreY3 :  0.655,
# # rnrRiskScoreY5 :  0.6425,
# # rnrSecYield :  0.5625,
# #  :  0.5775,
# # rnrSharpeRatioY10 :  0.505,
# # rnrSharpeRatioY15 :  0.35,
# # rnrSharpeRatioY3 :  0.465,
# # rnrSharpeRatioY5 :  0.54,
# print(y)
# # print('rating' + str(y['rnrRatingOverall']))
# # print('ret' + str(y['rnrRiskAdjustedReturnOverall']))
# # print('risk' + str(y['rnrRiskScoreOverall']))
# # print('sharpe' + str(y['rnrSharpeRatioY1']))
