import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR

def fit2nPandas(a, b, A, B):
    """put data into dataframe"""
    df1 = pd.DataFrame({str(A): a})
    df2 = pd.DataFrame({str(B): b})
    df = pd.concat([df1, df2], axis=1)
    return df

def fitVarData(a, b, A, B):
    """fits pandas dataframe into VAR model"""
    model = VAR(fit2nPandas(a, b, A, B))
    return model.fit()

def varForecast(a, b, A, B, step):
    """make VAR forecast for given steps"""
    model = fitVarData(a, b, A, B)
    forcast = model.forecast(model.y, steps=step)
    return forcast
