import easygui
import pandas as pd


def getInteger(msg, title):
    """displays dialog for displayed input"""
    try:
        val = int(easygui.enterbox(msg=msg, title=title,
            default='4'))
        return val
    except (ValueError):
        print('Please enter a number!')
        return getInteger(msg, title)
    except Exception as e:
        print('Error: ' + str(e.__class__) + ' during getInteger()')


def splitData(data):
    """split the data for upcomming forecast"""
    n = int(len(data) * 0.8)
    train = pd.DataFrame(data[0][:n])
    test = pd.DataFrame(data[0][n:])
    return train, test
