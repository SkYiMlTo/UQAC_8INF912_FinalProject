from multiprocessing.connection import Listener
from anomaly_detector import AnomalyDetector
from  utils import compute_features,save_events
from Const import *

address = ('localhost', 6000)     
listener = Listener(address,authkey=b'pepper')
conn = listener.accept()
print("Connection accepted from " + str(listener.last_accepted))
buffer =[]
fenbuffer =[]

TRAINING_MODE = False
ad = AnomalyDetector()
last_feat = LAST_FEN_INIT

while True:
    data = conn.recv()
    buffer.append(data)
    
    if len(buffer)>=WINSIZE:
        
        feat_extract = compute_features(buffer,last_feat)
        
        print(feat_extract)
        if not TRAINING_MODE and  ad.predict(feat_extract.reshape(1,-1)) == -1:
            #handle anomaly
            print("Anomaly detected")
        else :
            fenbuffer.append(feat_extract)
        last_feat = feat_extract
        save_events(buffer[:HOPSIZE])
        buffer = buffer[HOPSIZE:]

    if len(fenbuffer)>=TRAIN_SIZE:
        ad.update_model(fenbuffer)
        fenbuffer = []
    print(data)

