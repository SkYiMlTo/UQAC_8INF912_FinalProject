from multiprocessing.connection import Listener
from tabnanny import verbose
from anomaly_detector import AnomalyDetector
from  utils import compute_features,save_events
from Const import *
import signal

address = ('localhost', 6000)  

def wait_for_client(address):
    listener = Listener(address,authkey=b'pepper')
    conn = listener.accept()
    print("Connection accepted from " + str(listener.last_accepted))
    return conn
buffer =[]
fenbuffer =[]

TRAINING_MODE = True
ad = AnomalyDetector()
last_feat = LAST_FEN_INIT

verbose=False

conn = wait_for_client(address)

while True:
    try :
        data = conn.recv()
    except : 
        print("Connection lost")
        conn=wait_for_client(address)
        continue
    buffer.append(data)
    
    if len(buffer)>=WINSIZE:
        
        feat_extract,ldate= compute_features(buffer,last_feat)
        
        if verbose : print(feat_extract)
        print(ldate)
        if not TRAINING_MODE and  ad.predict(feat_extract.reshape(1,-1)) == -1:
            #handle anomaly
            print("Anomaly detected")
            
        else :
            fenbuffer.append(feat_extract)
        last_feat = feat_extract
        save_events(buffer[:HOPSIZE])
        buffer = buffer[HOPSIZE:]

    if len(fenbuffer)>=TRAIN_SIZE:
        print("Training")
        ad.update_model(fenbuffer)
        fenbuffer = []
    
    if verbose:
        print(data)

