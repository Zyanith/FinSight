import datetime
import numpy as np
from sklearn.svm import SVR

def formatTimeData (svrtime):
    """Convert datetime.datetime into 2D array"""
    for timeItem in time:
        svrtime.append(timeItem.strftime('%m%d%y%I%M'))
    return np.reshape(svrtime,(len(svrtime), 1))


def svrLinear (time, value):
    """Creating linear svr for prediction with timestamp"""
    svr_lin = SVR(kernel='linear', C=100, gamma='auto')
    print('Started fitting linear at: ' + datetime.datetime.now())
    svr_lin.fit(time,value)
    print('Ended fitting linear at: ' + datetime.datetime.now())
    return svr_lin


def svrPoly (time, value):
    """Creating poly svr for prediction with timestamp"""
    svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,
                   coef0=1)
    print('Started fitting poly at: ' + datetime.datetime.now())
    svr_poly.fit(time,value)
    print('Ended fitting poly at: ' + datetime.datetime.now())
    return svr_poly


def svrRBF (time, value):
    """Creating rbf svr for prediction with timestamp"""
    svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
    print('Started fitting rbf at: ' + datetime.datetime.now())
    svr_rbf.fit(time,value)
    print('Ended fitting rbf at: ' + datetime.datetime.now())
    return svr_rbf
