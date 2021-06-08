import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.api import VAR
from varForecasting import fitVarData

def plotPriceWithTrend (time, price, trend):
    """displays Cryptoprice with time and trend data"""
    # feed data lists into pandas dataframe
    df = pd.DataFrame({
        'time':time,
        'price':price,
        'trend':trend
    })

    # define matplotlib plot / gca stands for 'get current axis'
    # df.plot(x='time',y='price',ax=plt.gca())

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

    # display plot
    plt.show()

def plotPrice (time, price):
    """displays Cryptoprice with time"""
    # feed data lists into pandas dataframe
    df = pd.DataFrame({
        'time':time,
        'price':price
    })

    # define matplotlib plot / gca stands for 'get current axis'
    df.plot(x='time',y='price',ax=plt.gca())

    # display plot
    plt.show()


def plotCorelation(df, periods, corelation):
    """displays ACF or PACF for validation"""
    diff = df[0].diff(periods=periods).dropna()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))

    ax1.plot(diff)
    ax1.set_title('Difference ' + str(periods))
    ax2.set_ylim(0, 1)
    if corelation == 'acf':
        plot_acf(diff, ax=ax2)
    elif corelation == 'pacf':
        plot_pacf(diff, ax=ax2)
    else:
        print('corelation variable not valid exiting!')
        return None
    plt.show()


def plotResiduals(residuals):
    """displays the residuals of the ARIMA results"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))

    ax1.plot(residuals)
    ax2.hist(residuals, density=True)
    plt.show()


def plotForecastARIMA(test, fc, se, conf, steps):
    """displays the ARIMA forecast results"""
    fc = pd.Series(fc, index=test[:steps].index)
    lower = pd.Series(conf[:, 0], index=test[:steps].index)
    upper = pd.Series(conf[:, 1], index=test[:steps].index)

    plt.figure(figsize=(16, 8))
    plt.plot(test[:steps], label='actual')
    plt.plot(fc, label='forecast')
    plt.fill_between(lower.index, lower, upper, color='k', alpha=0.1)
    plt.title('Forecast vs Actual')
    plt.legend(loc='upper left')
    plt.show()

def plotForecastVAR(a, b, A, B, steps):
    model = fitVarData(a, b, A, B)
    model.plot_forecast(steps)
    plt.show()
