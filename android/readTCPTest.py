#!/usr/bin/python3
import socket
#import serial
import time
import sys
import numpy as np
import keras
from sklearn.metrics import confusion_matrix, precision_score
import pandas as pd
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8080))

gesturesC = {
    "relax":1,
    "extend":2,
    "fist":3,
    "one":4,
        "transition":5,
        "generic":-1
}

def getSerial():
	return s.recv(1).decode()

def getSerialBuf():
        buf = ""
        while len(buf.split(",")) != 5:
                buf = ""
                newData = ""
                while not ("\r\n" in buf):
                        newData = getSerial()
                        buf = buf + newData
                        #print(repr(newData))
                buf = buf.split("\r\n")[0]
#                print(len(buf.split(",")))
#                print(repr(buf))
        return buf

        
port = sys.argv[1]
fileOut = sys.argv[2] + "testML"
datafile = fileOut
saveFile = sys.argv[2] + 'modelSave2'

f = open(fileOut, "w")
fy = open(fileOut+"Y.csv", "a")

#ser = serial.Serial(port, 9600, timeout=1)

def getData(timeout, label):
#    n = 0
#    ti = time.time()
#    while time.time()-ti<timeout:
    #vthreei = pr[4]
    #tileLast=time.time()
    lastDelta=0
    timeI=time.time()
    reading = getSerialBuf().split(",")
    pr = [0,0,0,0,0,0,0,"",0]
    pr[0] = time.time()-timeI
    pr[1] = time.time()-trel
    pr[2] = int(reading[0])
    pr[3] = int(reading[1])
    pr[4] = int(reading[2])
    pr[5] = int(reading[3])
    pr[6] = int(reading[4])
    pr[7] = label
    pr[8] = gesturesC[label]
    #delta = pr[4] - vthreei
    #dprdt= (delta-lastDelta)/(1) #~0.01 s/loop
    #tileLast=time.time()
    #lastDelta=delta
    for i in pr:
        #print str(i)+",",
        f.write(str(i)+",")
    #print(pr)
    fx.write(str(pr[2])+","+str(pr[3])+","+str(pr[4])+","+str(pr[5])+","+str(pr[6])+"\n")
    fy.write(str(pr[8])+"\n")
    #if dprdt == 0:
    #    vthreei = pr[4]
    #print ""
    f.write("\n")


model = keras.models.load_model(saveFile)
gestures = {
    1: "relax",
    2: "extend",
    3: "fist",
    4: "one",
    5: "transition"
}
fx = ""
def predictML():
    global fx
    fx = open(fileOut+"X.csv", "a")
    getData(0,"generic")
    fx.close()
    #    try:
    x_data = pd.read_csv(datafile+"X.csv",names=['s1','s2','s3','s4','s5'])
    x_test = x_data[-500:]
#    print(x_test)
    y_pred = model.predict(x_test)
#    print(y_pred)
    rounded = [np.argmax(x) for x in y_pred]
#    print(rounded)
    print("Gesture: "+str(rounded[-1])+"; "+gestures[rounded[-1]])
    #    except:
    #        pass
            

print("delta Time, Unix Time, pr1, pr2, pr3, pr4, pr5, label")
f.write("delta Time, Unix Time, pr1, pr2, pr3, pr4, pr5, label\n")
trel = time.time()
print(trel)

continueQ = input("Start? [Y/n]: ")
if continueQ == "y" or continueQ == "" or continueQ == "Y":
    while True:
        predictML()
elif continueQ == "n" or continueQ == "N":
    continueQ = "n"
    
f.close()
