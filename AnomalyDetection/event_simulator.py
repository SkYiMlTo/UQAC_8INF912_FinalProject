import time
import pandas as pd 

import sys

from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey=b'pepper')




dir="data"
file =dir + "/" + "hh101.rawdata.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]

data= pd.DataFrame(columns=["Date", "Sensor", "Translate01", "Translate02", "Message", "SensorType"])

with open(file) as f:
    lines = f.readlines()
    
lines =[line.split("\t") for line in lines[int(0.90*len(lines)):]]
test = pd.DataFrame(lines,columns=["Date", "Sensor", "Translate01", "Translate02", "Message", "SensorType"])
test["Date"] = pd.to_datetime(test["Date"])



for i in range(len(test)):
    print(test.iloc[i])
    conn.send(test.iloc[i])
    sl =  (test.iloc[i+1].Date - test.iloc[i].Date).total_seconds()/100
    print(sl)
    time.sleep(sl)
    
   

conn.close()