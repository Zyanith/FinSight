import matplotlib.pyplot as plt
import pandas as pd


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
