import pandas as pd

def getdeliveriesdata():
    return pd.read_csv("data/deliveries.csv")

def getmatchesdata():
    return pd.read_csv("data/matches.csv")

def getmatchdatabyyr(yr):
    return getmatchesdata()[getmatchesdata()['season'] == yr]    

