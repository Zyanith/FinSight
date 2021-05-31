import pandas as pd
from pytrends.request import TrendReq


def getGoogleTrendsDay (keyword, days):
    """gets googleTrend data for every hour of the last 7 days based on keyword,
        see https://pypi.org/project/pytrends/"""
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[keyword], cat=0, timeframe='now '+days+'-d')
    return pytrends.interest_over_time()
