import datetime
import numpy as np
from coingeckoAPI import getCryptoData
from googleTrendsAPI import getGoogleTrendsDay
from plotData import plotPriceWithTrend, plotPrice
from supprtVectorRegression import formatTimeData, svrLinear, svrPoly, svrRBF


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

# plot data
# plotPrice(time, price)
plotPriceWithTrend(time, price, trend)

# converting time to be used in svr
svrtime = formatTimeData(time)

# intialicing and fitting prediciton functions
svr_lin = svrLinear(time, price)
svr_poly = svrPoly(time, price)
svr_rbf = svrRBF(time, price)


# make prediction
dayToPredict = datetime.datetime.now()
predictedDay = formatTimeData(dayToPredict)
print('The Linear SVR prediction:', svr_lin.predict(predictedDay))
print('The Polynomial SVR prediction:', svr_poly.predict(predictedDay))
print('The RBF SVR prediction:', svr_rbf.predict(predictedDay))
