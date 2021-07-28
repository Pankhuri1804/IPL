import data as d

def getwinsperteamperseason(yr):
    data =  d.getmatchesdata()
    tmnm = data[data['season'] == yr].groupby('season')['winner'].value_counts().head(4)
    return tmnm.to_json()

def getmaxtosswinnerteam(yr):
    data =  d.getmatchesdata()
    tmnm = data[data['season'] == yr]['toss_winner'].value_counts().head(1)
    print(tmnm)
    return tmnm

def getmaxplayerofmatch(yr):
    data =  d.getmatchesdata()
    plynm = data[data['season'] == yr]['player_of_match'].value_counts().head(1)
    return plynm

def getmaxwinnerteam(yr):
    data =  d.getmatchesdata()
    tmnm = data[data['season'] == yr]['winner'].value_counts().head(1) 
    return tmnm

def locationforwinnerteam(yr):
    tmnm = getmaxwinnerteam(yr).head(1).keys()[0]
    data = d.getmatchesdata()
    citynm = data[(data['winner'] == tmnm) & (data['season'] == yr)].groupby('city')['city'].count().sort_values(ascending=False).head(1).keys()[0]
    return citynm

def percofbat(yr):
    data = d.getmatchesdata()
    bat = data[data['season'] == yr]['toss_decision'].value_counts()['bat']
    totaldecision = data[data['season'] == yr]['toss_decision'].count()
    print(str(bat) + " " + str(totaldecision))
    perc = round((bat/totaldecision)*100,2)
    return perc

def getlocationmaxmatch(yr):
    data =  d.getmatchesdata()
    citynm = data[data['season'] == yr]['city'].value_counts().head(1).keys()[0]
    return citynm     

def highestmarginrunwin(yr):
    data =  d.getmatchesdata()
    teamnm = data[data['season'] == yr].sort_values(by='win_by_runs',ascending=False).head(1)['winner'].values[0]
    return teamnm

def highestmarginwktwin(yr):
    data =  d.getmatchesdata()
    teamnm = data[data['season'] == yr].sort_values(by='win_by_wickets',ascending=False).head(1)['winner'].values[0]
    return teamnm   

def getwinnerteambytossandmatch(yr):
    data =  d.getmatchesdata()
    teamnm = data[(data['season'] == yr) & (data['toss_winner'] == data['winner'])].groupby('winner')['winner'].count()
    return teamnm     

def batsmanwithmostruns(yr):
    match = d.getmatchesdata()
    deliveries = d.getdeliveriesdata()
    consideredmatch = match[match['season'] == yr]['id']
    sumdata = deliveries[deliveries['match_id'].isin(consideredmatch)].groupby('batsman')['total_runs'].sum('total_runs')
    maxrunplayer = sumdata.idxmax()
    maxrun = sumdata.max()
    returnval = {"Player" : maxrunplayer, "TotalRuns": str(maxrun)}
    return returnval   

def fielderwithmostcaughts(yr):
    match = d.getmatchesdata()
    deliveries = d.getdeliveriesdata()
    consideredmatch = match[match['season'] == yr]['id']
    sumdata = deliveries[(deliveries['match_id'].isin(consideredmatch)) & (deliveries['player_dismissed'].notnull())].groupby('fielder')['fielder'].value_counts()
    bowler = sumdata.idxmax()[0]
    maxwkt = sumdata.max()
    returnval = {"Fielder" : bowler, "TotalWickets": str(maxwkt)}
    return returnval
