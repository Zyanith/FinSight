import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
from utils import splitData

def fit1nPandasAndTest(a, A):
    df = pd.DataFrame({str(A): a})
    return adjustData(df)

def fit2nPandas(df1, df2):
    """put data into dataframe"""
    return pd.concat([df1, df2], axis=1)

def fitVarData(a, b, A, B):
    """fits pandas dataframe into VAR model"""
    model = VAR(fit2nPandas(fit1nPandasAndTest(a, A), fit1nPandasAndTest(b, B)))
    return model.fit()

def varForecast(a, b, A, B, step):
    """make VAR forecast for given steps"""
    model = fitVarData(a, b, A, B)
    forcast = model.forecast(model.y, steps=step)
    return forcast

def checkIfStationary(data, signif=0.05):
    dftest = adfuller(data, autolag='AIC')
    adf = pd.Series(dftest[0:4], index=['Test Statistic','p-value','# Lags',
        '# Observations'])

    for key,value in dftest[4].items():
       adf['Critical Value (%s)'%key] = value
    p = adf['p-value']
    #print(adf)
    #print(p)
    if p <= signif:
        return True
    else:
        return False


def adjustData(data):
    while data is checkIfStationary(data):
        if data is checkIfStationary(data):
            data = data.diff().dropna()
        else:
            return data.diff().dropna()
    return data
