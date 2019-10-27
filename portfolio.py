

class Portfolio:
    

    def __init__(self, risk,initial_companies):
        
        self.portfolio = {}
        self.returns = 0
        self.other = 0

        if risk == 0:
            self.portfolio['CASH-USD'] = [.2,'c']
            self.cashprop = .2
            self.bondsprop = .7
            self.stocksprop = .1
            self.allocate_random('bonds', .7, [], 'b')
            self.allocate_random('stocks', .1, initial_companies, 's')
            self.actual = ''
            self.date = 0
            
        if risk == 1:
            self.portfolio['CASH-USD'] = [.1, 'c']
            self.cashprop = .1
            self.bondsprop = .4
            self.stocksprop = .4
            self.actualprop = ''
            self.allocate_random('bonds', .4, [], 'b')
            self.allocate_random('stocks', .4, initial_companies, 's')
            self.date = 0

        if risk == 2:        
            self.cashprop = .0
            self.portfolio['CASH-USD'] = [.0,'c']
            self.bondsprop = .3
            self.stocksprop = .7
            self.actual = ''
            self.allocate_random('bonds', .3, [], 'b')
            self.allocate_random('stocks', .7, initial_companies, 's')
            self.date = 0

    def allocate_random(self,type, type_prop, initial_companies, char):
        
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
            self.portfolio[stock[0]] = [type_prop * proportion[counter] , char]
            counter +=1        
        print(self.portfolio)
         
    def blackrockify(self):
        mystr=''
        for company in self.portfolio:
            compstr = '~'.join([company,str(self.portfolio[company][0])])
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
        
        if self.returns == self.other:
            self.returns = vy['marketReturnM2']
            self.other = vy['marketReturnM3']
        else:
            self.returns = vy['marketReturnM1']
            self.other = vy['marketReturnM2']
        print(self.returns)
        print(self.other)
        self.recommend()
        print(self.portfolio)
    def recommend(self):
        import json, csv
        if self.other > self.returns:
            self.returns = self.other
            return(None)
        else:
            if self.date == 0:
                start = self.y['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['returns']['startDate']
            else:
                start = self.date
            #end = start + 100
            
            if str(start)[4:6] == '12':
                end = start + 10000 - 1100
            else:
                end = start + 100
            self.date = end
            with open('vix.csv', mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                vix_data = {}
                for date, op, hi, lo, cl, adj, v in csv_reader:
                    vix_data[date] = float(adj)            
            
            start = str(start)[:4] + '-' + str(start)[4:6] + '-' + '01'
            end = str(end)[:4] + '-' + str(end)[4:6] + '-' + '01'
            #if difference is smaller, it means that vol decreased, move to equity
            diff = vix_data[end] - vix_data[start]
            #realloc by vix / .2
            diff *= .1
            #from decimal import Decimal
            #diff = Decimal(diff)
            diff = round(diff, 2)
            print(diff)
            #adjust
            if (diff >= 0):
                new_bond = self.bondsprop - diff
                new_stock = self.stocksprop + diff
                for company in self.portfolio.keys():
                    if self.portfolio[company][1] == 'b':
                        self.portfolio[company][0] = new_bond * self.portfolio[company][0] / self.bondsprop
                    if self.portfolio[company][1] == 's':
                        self.portfolio[company][0] = new_stock * self.portfolio[company][0] / self.stocksprop
                self.stocksprop = new_stock
                self.bondsprop = new_bond
            elif (diff < 0):
                new_bond = self.bondsprop + diff
                new_stock = self.stocksprop - diff
                for company in self.portfolio.keys():
                    if self.portfolio[company][1] == 'b':
                        self.portfolio[company][0] = new_bond * self.portfolio[company][0] / self.bondsprop
                    if self.portfolio[company][1] == 's':
                        self.portfolio[company][0] = new_stock * self.portfolio[company][0] / self.stocksprop
                self.stocksprop = new_stock
                self.bondsprop = new_bond
        
if __name__ == "__main__":
    port = Portfolio(2,['AAPL'])
    port.get_market_returns()
    for x in range(5):
        port.get_market_returns()








