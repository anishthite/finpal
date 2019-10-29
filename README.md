# FinPal

## A Hackathon project made in @HackGT 6 

##### _The goal_
Finpal is a chatbot which aims to help people who are new to investing jump right in.  New investors will liekly not know how to allocate certain stocks, which stocks are safe, and what bonds and other securities are, so we wanted to make a tool which could make them a starter portfolio.  

##### _How it works_
When the user enters the website, he is presented with a chatbot interface.  After the user confirms he wants to try the portfolio allocation tool, the bot asks him if he know their relative risk level that he wants to invest with.  If he doesn't know, the bot asks him a 13-question survey which was created by Rutgers for investing risk assesment, out of which the bot generates a risk factor and begins to allocate stocks.  The bot also asks the user if he already has specific stocks in mind, and modifies the allocation to include any such preferences.  Then, the bot sends a simulation of the portfolio over time through a series of text messages to the user.  

##### _What did we use_
We used the Blackrock API to gather stock data on various companies and indicies.  The VIX is usually a factor in investments, so we used that and performance oveer time of the stock itself to create allocations using past data.  The chatbot was made using Google Dialogflow which interfaced with our algorithms on a Flask server using ngrok https tunneling.  After allocation is done, we used SMTP and SMS APIs for major carriers to send the text messages to the end user to simulate portfolio performance

##### _What can we work on_
Ideally, the tool would be live and allocations would happen dynamically.  We could also manage the portfolio directly instead of simply simulating it if we had the legal/API capabilities to do so.  Even if that weren't the case, allowing users to create a portfolio and have it simulating live in real time would definitely help new investors until they get a handle of the market.  Finally, we can always improve our tool by researching new studies on portfolio allocation, trading bots, and other financial/AI research to improve how our bot allocates stocks.
