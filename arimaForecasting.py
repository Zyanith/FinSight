import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima.utils import ndiffs
from utils import getInteger
from plotData import plotCorelation, plotResiduals, plotForecast


def ADFtest(df):
    """using ADF to check if the price series is stationary"""
    ADF = adfuller(df[0].dropna())
    print("ADF: " + str(ADF[0]))
    print("p-value: " + str(ADF[1]))
    if ADF[1] > 0.05:
        print('p-value > 0.05!')
        print('price series is not stationary')
    else:
        print('price series is stationary')
    return ADF


def getADF(df):
    """get ARIMA differencing term"""
    return ndiffs(df[0], test='adf')


def getAR(df, periods):
    """displays Partial Autocorelation (PACF) plot for Auto Regression (AR)
    selection with dialog"""
    plotCorelation(df, periods, 'pacf')
    return getInteger('Please enter your selected AR value!', 'AR value')


def getMA(df, periods):
    """displays Autocorelation (ACF) plot for Moving Average (MA) selection
    with dialog"""
    plotCorelation(df, periods, 'acf')
    return getInteger('Please enter your selected MA value!', 'MA value')


def fitARIMA(df, p, d, q):
    """fit variables into ARIMA model"""
    model = ARIMA(df[0], order=(p, d, q))
    return model.fit(disp=0)


def ARIMAcall(df):
    """main function to make ARIMA model"""
    d = getADF(df)
    p = getAR(df, d)
    q = getMA(df, d)
    model = fitARIMA(df, p, d, q)
    print(model.summary())
    return model


def getResidualErrors(results):
    """displays residuals errors for validation"""
    residuals = pd.DataFrame(results.resid)
    plotResiduals(residuals)


def plotResults(results, steps):
    """displays Prediction and actual values for comparison"""
    results.plot_predict(start=1, end=steps, dynamic=False)
    plt.show()


def trainedARIMAcall(df, step):
    """main function to make trained ARIMA model"""
    train, test = splitData(df)

    d = getADF(train)
    p = getAR(train, d)
    q = getMA(train, d)
    model = fitARIMA(train, p, d, q)
    print(model.summary())
    fc, se, conf = model.forecast(step)
    return test, fc, se, conf


def splitData(data):
    """split the data for upcomming forecast"""
    n = int(len(data) * 0.8)
    train = pd.DataFrame(data[0][:n])
    test = pd.DataFrame(data[0][n:])
    return train, test


def plotForecastResults(df, steps):
    """displayes the ARIMA forecast results"""
    test, fc, se, conf = trainedARIMAcall(df, steps)
    plotForecast(test, fc, se, conf, steps)
