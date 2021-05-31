import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np
from coingeckoAPI import getCryptoData
from googleTrendsAPI import getGoogleTrendsDay
from plotData import plotPriceWithTrend, plotPrice


# Get price and trends data
bitcoinPrice = getCryptoData('bitcoin', 'eur', '7')
bitcoinTrends = getGoogleTrendsDay('bitcoin') # API limit 1 or 7 days only

# initialise variables
time = []
price = []
trend = list(np.array(bitcoinTrends)[0:,0:1])

# format data to usable lists
for day in bitcoinPrice['prices']:
    # cuts ms
    time.append(datetime.datetime.fromtimestamp(int(day[0] / 1000)))
    price.append(day[1])

# cut unnecessary data
time = time[:len(trend)]
price = price[:len(trend)]

# plot data
# plotPrice(time, price)
plotPriceWithTrend(time, price, trend)
