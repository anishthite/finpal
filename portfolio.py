

class Portfolio:
    

    def __init__(self, risk,initial_companies):
        
        self.portfolio = {}

        if risk == 0:
            self.portfolio['CASH-USD'] = .2
            self.cashprop = .2
            self.bondsprop = .7
            self.stocksprop = .1
            self.allocate_random('bonds', .7, [])
            self.allocate_random('stocks', .1, initial_companies)
            self.actual = ''
            
        if risk == 1:
            self.portfolio['CASH-USD'] = .1
            self.cashprop = .1
            self.bondsprop = .4
            self.stocksprop = .4
            self.actualprop = ''
            self.allocate_random('bonds', .4, [])
            self.allocate_random('stocks', .4, initial_companies)

        if risk == 2:        
            self.cashprop = .0
            self.portfolio['CASH-USD'] = .0
            self.bondsprop = .3
            self.stocksprop = .7
            self.actual = ''
            self.allocate_random('bonds', .3, [])
            self.allocate_random('stocks', .7, initial_companies)

    def allocate_random(self,type, type_prop, initial_companies):
        
        possible_tickers = []
        import csv
        import random
        with open(type + '.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            possible_tickers = list(csv_reader)

        if initial_companies != []:
            for company in initial_companies:
                possible_tickers.append([company])

        proportion = random.sample(range(0,10), len(possible_tickers))
        listsum = sum(proportion)
        #print(listsum)
        for x in range(len(proportion)):
            element = proportion[x]
            element /= listsum
            proportion[x] = element
        #print(proportion)
        #print(sum(proportion))
        counter = 0
        mydic = {}
        for stock in possible_tickers:
            self.portfolio[stock[0]] = type_prop * proportion[counter]
            counter +=1        
        print(self.portfolio)
         
    def blackrockify(self):
        mystr=''
        for company in self.portfolio:
            compstr = '~'.join([company,str(self.portfolio[company])])
            mystr = ''.join([mystr,compstr,'|'])
        return mystr

    def get_market_returns(self):
        import requests, json
        mystr = self.blackrockify()
        portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : mystr})
        portfolioAnalysisRequest.text # get in text string format
        portfolioAnalysisRequest.json # get as json object
        self.y = json.loads(portfolioAnalysisRequest.text)
        vy = self.y['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['weightedAveragePerformance']
        self.returns = vy['marketReturnM1']
        self.other = vy['marketReturnM2']
        print(self.returns)
        print(self.other)
        self.recommend()
        
    def recommend(self):
        import json, csv
        # if self.other > self.returns:
        #     return(None)
        # else:
        start = self.y['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['startDate']
        with open('vix.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            csv_reader = list(csv_reader))
        start = str(start)[:4] + '-' + str(start)[4:6] + '-' + '01'
        print(csvreader[start])
        
if __name__ == "__main__":
    port = Portfolio(2,['AAPL','GOOG'])
    port.get_market_returns()








