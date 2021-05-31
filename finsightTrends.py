#!/usr/bin/env python
# coding: utf-8

# In[358]:


import json
import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import tweepy
import datetime as dt
import numpy as np
import array as arr


#how many days back?
days = 500


def getData (coin, currency, daysback):
    """API call to coingecko for historical coin prices"""
    api_url = ('https://api.coingecko.com/api/v3/coins/' + str(coin) +
        '/market_chart?vs_currency=' + str(currency) +
        '&days=' + str(daysback))

    response = requests.get(api_url).text
    return json.loads(response)

# Get coin data
data = getData('bitcoin', 'eur', days)

# initialise variables
time = []
price = []
trend = []

#reading in csv
trends_df = pd.read_csv("googleTrends5y.csv", header = 0)

# format data to usable lists
for day in data['prices']:
    # cuts ms
    date_time = datetime.date.fromtimestamp(int(day[0] / 1000)).strftime("%Y-%m-%d")
    if date_time <= trends_df["Week"].max():
        time.append(datetime.datetime.fromtimestamp(int(day[0] / 1000)))
        price.append(day[1])

        #be wary of list length so only add trend for entire week in a loop(to avoid index errors)
        if date_time in trends_df.values:
                current_trend = trends_df.loc[trends_df['Week'] == date_time, 'bitcoin: (Worldwide)'].iloc[0]
                for i in range(7):
                    trend.append(current_trend)


#remove extra list entries from "trend" so lists have same length for DF
difference  =  len(trend) - len(time)
trend = trend[:len(trend)-difference]
#do the same for other two lists if they're the bigger ones (delete first entries instead)
if difference < 0:
    difference  =  len(time) - len(trend)
    del time[:difference]
    del price[:difference]

# feed data lists into pandas dataframe
df = pd.DataFrame({
    'time':time,
    'price':price,
    'trend':trend
})

#save it as a csv file
df.to_csv('./new.csv', index = False)


##plot


print("As per google: Numbers represent search interest relative to the highest point on the chart for the given region and time. A value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term.")
##subplots
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time')
ax1.set_ylabel('bitcoin price', color=color)
ax1.plot(df.time, df.price, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() #2nd axis

color = 'tab:blue'
ax2.set_ylabel('google trend %', color=color)
ax2.plot(df.time, df.trend, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.autofmt_xdate()
fig.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:
