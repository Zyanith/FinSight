#!/usr/bin/env python
# coding: utf-8

# In[87]:


import json
import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import tweepy
import datetime as dt
import numpy as np
##!pip install tweepy

#put in your own
consumer_key = "Lnez7Mxc5qL96rZglloz5uLE5"
consumer_secret = "yR1UtmIJwsREJrj2AKcqKEAD5BGiRBXDT38yb25P4kso2dqjke"
access_token = "1395193313435717634-8d8ViSCSx83PCa0vWcsqCbCQGowzkl"
access_token_secret = "Wl81FrBwuja80fTxY6uJ5zIp9FZGJosIpeo89HVRXD4IJ"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)

#tweet part
# the ID of the status
id = 1394001894809427971
  
# fetching the status
user = api.get_status(id)
  
# fetching the created_at attribute
created_at = user.created_at 
print("The status was created at : " + str(created_at))

#calc days
d0 = date.today()
d1 = date(created_at.year,created_at.month,created_at.day)
delta = d0 - d1
days = delta.days + 90

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

# format data to usable lists
for day in data['prices']:
    # cuts ms
  
    time.append(datetime.datetime.fromtimestamp(int(day[0] / 1000)))
    price.append(day[1])

# feed data lists into pandas dataframe
df = pd.DataFrame({
    'time':time,
    'price':price
})

#find matching date and value and assign price at tweet date to y val so we can add the dot to the plot
df['time'] = pd.to_datetime(df['time'])
y_val = df.iloc[np.where((df['time'].dt.day==created_at.day) & (df['time'].dt.month==created_at.month) & (df['time'].dt.year==created_at.year))]['price']

##plot

# define matplotlib plot / gca stands for 'get current axis'
df.plot(x='time',y='price',ax=plt.gca())
#add tweet date
plt.plot(created_at, y_val, 'ro')
plt.text(created_at, y_val,user.user.name)

# display plot
plt.show()



# In[ ]:




