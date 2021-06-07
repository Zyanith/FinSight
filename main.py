import datetime
import numpy as np
import pandas as pd
from coingeckoAPI import getCryptoData
from googleTrendsAPI import getGoogleTrendsDay
from plotData import plotPriceWithTrend, plotPrice
from supportVectorRegression import formatTimeData, svrLinear, svrPoly, svrRBF
from arimaForecasting import ADFtest, ARIMAcall, getResidualErrors, plotResults

# Get price and trends data
bitcoinPrice = getCryptoData('bitcoin', 'eur', '1')
bitcoinTrends = getGoogleTrendsDay('bitcoin', '1') # API limit 1 or 7 days only

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

price_df = pd.DataFrame(price)
#price_df.columns(['price'])


# plot data
# plotPrice(time, price)
# plotPriceWithTrend(time, price, trend)

# ARIMA forcast
ADF = ADFtest(price_df)
ARIMAmodell = ARIMAcall(price_df)
getResidualErrors(ARIMAmodell)
plotResults(ARIMAmodell, 170)
