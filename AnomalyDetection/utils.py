import numpy as np
import pandas as pd
import os
from Const import FEAT_NAMES

def save_events(events):
    #append series in event to log file
    df =pd.DataFrame(events)
    df.loc[:, "SensorType"] = df["SensorType"].apply(lambda x : x.replace('\n', '\\n'))
    #check if file exists
    if not os.path.isfile("log.csv"):
        df.to_csv("log.csv",index=False)
    df.to_csv("log.csv",mode='a',header=False,index=False,)



MotionSensorlist = [m for m in FEAT_NAMES if "M" in m]
DoorSensorlist = [d for d in FEAT_NAMES if "D" in d]
LightSensorlist = [l for l in FEAT_NAMES if "LS" in l]
TempSensorlist = [t for t in FEAT_NAMES if "T" in t]

def compute_features(fen,last_features) :
    
    fen = pd.DataFrame(fen)

    #heure 
    last_date = fen["Date"].iloc[-1]
    last_hour = last_date.hour + last_date.minute/60
    duration = (fen["Date"].iloc[-1] - fen["Date"].iloc[0]).seconds

    #jour de la semaine
    week_day = last_date.weekday()
    month = last_date.month
    features = [last_hour, month,week_day, duration]
    #motion sensor
    
    i=len(features)
    for m in MotionSensorlist:
        if m in fen["Sensor"].tolist():
            if fen[fen["Sensor"]==m].iloc[-1]["Message"] == "ON":
                features.append(1)
            else:
                features.append(-1)
        else:
            features.append(last_features[i])
        i+=1

    

    for d in DoorSensorlist:
        if d in fen["Sensor"].tolist():
            if fen[fen["Sensor"]==d].iloc[-1]["Message"] == "OPEN":
                features.append(1)
            else:
                features.append(-1)
        else:
            features.append(last_features[i])
        i+=1
    
    
    for l in LightSensorlist:
        if l in fen["Sensor"].tolist():
            features.append(int(fen[fen["Sensor"]==l].iloc[-1]["Message"])/100.)
        else:
            features.append(last_features[i])
        i+=1
    
    for t in TempSensorlist:
        if t in fen["Sensor"].tolist():
            features.append(float(fen[fen["Sensor"]==t].iloc[-1]["Message"])/50.)
        else:
            features.append(last_features[i])
        i+=1
    
    
    
    
    return np.array(features),last_date

