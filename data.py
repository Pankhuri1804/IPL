import pandas as pd

def getdeliveriesdata():
    return pd.read_csv("IPL/data/deliveries.csv")

def getmatchesdata():
    return pd.read_csv("IPL/data/matches.csv")

