import datetime
import numpy as np
import pandas as pd
from coingeckoAPI import getCryptoData
from googleTrendsAPI import getGoogleTrendsDay
from plotData import plotPriceWithTrend, plotPrice, plotForecastVAR
from arimaForecasting import ARIMAcall, getResidualErrors, \
    plotResults, plotForecastResultsARIMA
from varForecasting import varForecast


# Get price and trends data
bitcoinPrice = getCryptoData('bitcoin', 'eur', '7')
bitcoinTrends = getGoogleTrendsDay('bitcoin', '7') # API limit 1 or 7 days only

# initialise variables
time = []
price = []
trend = []
#trend = np.asarray(bitcoinTrends)

for data in np.asarray(bitcoinTrends)[0:,0:1]:
    trend.append(data[0])


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
# plotPriceWithTrend(time, price, trend)

# ARIMA forcast
# price_df = pd.DataFrame(price)
# price_df.columns(['price'])
# ARIMAmodell = ARIMAcall(price_df)
# getResidualErrors(ARIMAmodell)
# plotResults(ARIMAmodell, 170)

# ARIMA forcast with 80% Training Data & 20% Testing
# plotForecastResultsARIMA(price_df, 30)

# VAR forcast
# print(varForecast(price, trend, 'price', 'trend', 10))
plotForecastVAR(price, trend, 'price', 'trend', 10)
