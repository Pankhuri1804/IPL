from flask import Flask, request
import service as ser
import json

app =  Flask(__name__)
app.config["DEBUG"] = True


@app.route("/top4team")
def getwinsperteamperseason():
    yr = request.args.get("yr")
    tmnm = ser.getwinsperteamperseason(int(yr))
    return tmnm

@app.route("/maxtosswinnerteam")
def getmaxtosswinnerteam():
    yr = request.args.get("yr")
    tmnm = ser.getmaxtosswinnerteam(int(yr))
    return json.dumps(tmnm.to_dict())

@app.route("/maxplayerofmatch")
def getmaxplayerofmatch():
    yr = request.args.get("yr")
    tmnm = ser.getmaxplayerofmatch(int(yr))
    return tmnm.to_json()

@app.route("/maxwinnerteam")
def getmaxwinnerteam():
    yr = request.args.get("yr")
    tmnm = ser.getmaxwinnerteam(int(yr))
    return tmnm.to_json()   

@app.route("/locationforwinnerteam")
def locationforwinnerteam():
    yr = request.args.get("yr")
    city = ser.locationforwinnerteam(int(yr))
    return city            

@app.route("/percentofbatting")
def percofbat():
    yr = request.args.get("yr")
    prc = ser.percofbat(int(yr))
    return str(prc)

@app.route("/maxmatchlocation")
def getlocationmaxmatch():
    yr = request.args.get("yr")
    city = ser.getlocationmaxmatch(int(yr))
    return city   

@app.route("/highestmarginbyrunwinner")
def highestmarginrunwin():
    yr = request.args.get("yr")
    teamnm = ser.highestmarginrunwin(int(yr))
    return teamnm  

@app.route("/highestmarginwktwin")
def highestmarginwktwin():
    yr = request.args.get("yr")
    teamnm = ser.highestmarginwktwin(int(yr))
    return teamnm    

@app.route("/getwinnerteambytossandmatch")
def getwinnerteambytossandmatch():
    yr = request.args.get("yr")
    teamnm = ser.getwinnerteambytossandmatch(int(yr))
    return json.dumps(teamnm.to_dict())

app.run(host ='0.0.0.0', port = 5000, debug = True)


