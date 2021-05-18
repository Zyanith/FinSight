import json
import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime

def getData (coin, currency, daysback):
    """API call to coingecko for historical coin prices"""
    api_url = ('https://api.coingecko.com/api/v3/coins/' + str(coin) +
        '/market_chart?vs_currency=' + str(currency) +
        '&days=' + str(daysback))

    response = requests.get(api_url).text
    return json.loads(response)

# Get coin data
data = getData('bitcoin', 'eur', '2')

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

# define matplotlib plot / gca stands for 'get current axis'
df.plot(x='time',y='price',ax=plt.gca())

# display plot
plt.show()
