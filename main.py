import datetime
import numpy as np
import pandas as pd
from coingeckoAPI import getCryptoData
from googleTrendsAPI import getGoogleTrendsDay
from plotData import plotPriceWithTrend, plotPrice, plotForecastVAR
from arimaForecasting import ARIMAcall, getResidualErrors, \
    plotResults, plotForecastResultsARIMA
from varForecasting import varForecast

def finalPlot():
    """displayes the price graph with and without the trends"""
    bitcoinPrice = getCryptoData('bitcoin', 'eur', '1')
    bitcoinTrends = getGoogleTrendsDay('bitcoin', '1') # API 1 or 7 days only
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
    plotPrice(time, price)
    plotPriceWithTrend(time, price, trend)


def finalARIMA():
    """displays the stationary ARIMA model"""
    # Get price and trends data
    bitcoinPrice = getCryptoData('bitcoin', 'eur', '1')
    bitcoinTrends = getGoogleTrendsDay('bitcoin', '1') # API 1 or 7 days only

    # initialise variables
    price = []
    trend = list(np.array(bitcoinTrends)[0:,0:1])

    # format data to usable lists
    for day in bitcoinPrice['prices']:
        # cuts ms
        price.append(day[1])

    # cut unnecessary data
    price = price[:len(trend)]

    price_df = pd.DataFrame(price)
    #price_df.columns(['price'])

    # ARIMA forcast
    ARIMAmodell = ARIMAcall(price_df)
    getResidualErrors(ARIMAmodell)
    plotResults(ARIMAmodell, 170)

def finalARIMAwithTesting():
    """displays the forcast for the ARIMA model"""
    # Get price and trends data
    bitcoinPrice = getCryptoData('bitcoin', 'eur', '1')
    bitcoinTrends = getGoogleTrendsDay('bitcoin', '1') # API 1 or 7 days only

    # initialise variables
    price = []
    trend = list(np.array(bitcoinTrends)[0:,0:1])

    # format data to usable lists
    for day in bitcoinPrice['prices']:
        # cuts ms
        price.append(day[1])

    # cut unnecessary data
    price = price[:len(trend)]

    price_df = pd.DataFrame(price)

    # ARIMA forcast with 80% Training Data & 20% Testing
    plotForecastResultsARIMA(price_df, 30)

def finalVAR():
    """displays the forecast for the VAR model"""
    # Get price and trends data
    bitcoinPrice = getCryptoData('bitcoin', 'eur', '7')
    bitcoinTrends = getGoogleTrendsDay('bitcoin', '7') # API 1 or 7 days only

    # initialise variables
    price = []
    trend = []

    for data in np.asarray(bitcoinTrends)[0:,0:1]:
        trend.append(data[0])

    # format data to usable lists
    for day in bitcoinPrice['prices']:
        # cuts ms
        price.append(day[1])

    # cut unnecessary data
    price = price[:len(trend)]

    # VAR forcast
    plotForecastVAR(price, trend, 'price', 'trend', 10)


finalPlot()
finalARIMA()
finalARIMAwithTesting()
finalVAR()
