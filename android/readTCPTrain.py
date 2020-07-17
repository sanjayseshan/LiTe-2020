#!/usr/bin/python3
import socket
#import serial
import time
import sys
import numpy as np
import keras
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from sklearn.metrics import confusion_matrix, precision_score
from sklearn.model_selection import train_test_split
from keras.layers import Dense,Dropout
from keras.regularizers import l2
import matplotlib.pyplot as plt
import pandas as pd

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8080))

gesturesC = {
    "relax":1,
    "extend":2,
    "fist":3,
    "one":4,
    "transition":5
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
fileOut = sys.argv[2]


f = open(fileOut, "w")
fx = open(fileOut+"X.csv", "w")
fy = open(fileOut+"Y.csv", "w")

#ser = serial.Serial(port, 9600, timeout=1)

def getData(timeout, label):
#    n = 0
#    ti = time.time()
#    while time.time()-ti<timeout:
    #vthreei = pr[4]
    #tileLast=time.time()
    lastDelta=0
    timeI=time.time()
    while time.time()-timeI < timeout:
#        try:
            reading = getSerialBuf().split(",")
#            print(reading)
#            reading = getSerialBuf().split(",")
#            reading = getSerialBuf().split(",")
#            reading = getSerialBuf().split(",")
#            reading = getSerialBuf().split(",")
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
            print(pr)
            fx.write(str(pr[2])+","+str(pr[3])+","+str(pr[4])+","+str(pr[5])+","+str(pr[6])+"\n")
            fy.write(str(pr[8])+"\n")
            #if dprdt == 0:
            #    vthreei = pr[4]
            #print ""
            f.write("\n")
            #time.sleep(0.05)
#        except:
#            pass

#gestures = ["fist", "extend", "one", "two", "three", "four", "five", "spiderman", "vulcan", "index in", "middle in", "ring in", "little in", "thumb in", "lift up", "lift down"]


def runGesture(gesture):
        getData(5,"relax")
        getData(2,"transition")
        getData(5,gesture)
        getData(2,"transition")
        getData(5,"relax")
        

#gestures=["relax","transition","extend","transition","relax"]

gestures = ["fist", "extend", "one"]

print("delta Time, Unix Time, pr1, pr2, pr3, pr4, pr5, label, numLabel")
f.write("delta Time, Unix Time, pr1, pr2, pr3, pr4, pr5, label, numLabel\n")
trel = time.time()
print(trel)

for gesture in gestures:
    continueQ = input("Do "+gesture+"? [Y/n]: ")
    if continueQ == "y" or continueQ == "" or continueQ == "Y":
        runGesture(gesture)
#            while True:
#                    print(getSerialBuf().split(","))
    elif continueQ == "n" or continueQ == "N":
        continueQ = "n"
    
f.close()
fx.close()
fy.close()

datafile = fileOut

x_data = pd.read_csv(datafile+"X.csv",names=['s1','s2','s3','s4','s5'])
y_dataR = np.genfromtxt(datafile+"Y.csv",delimiter=',',dtype=int)
num_classes = np.max(y_dataR) + 1
y_data = keras.utils.to_categorical(y_dataR, num_classes)
#x_train, x_test, y_train, y_test = train_test_split(x_data,y_data, test_size=0.20, random_state=0)
x_train = x_data
x_test = x_data[880:]
y_train = y_data
y_test = y_data[880:]
x_train.shape,y_train.shape,x_test.shape,y_test.shape

#defifne a sequentail Model
model = Sequential()
#Hidden Layer-1
model.add(Dense(100,activation='relu',input_dim=5,kernel_regularizer=l2(0.01)))
model.add(Dropout(0.3, noise_shape=None, seed=None))

#Hidden Layer-2
model.add(Dense(100,activation = 'relu',kernel_regularizer=l2(0.01)))
model.add(Dropout(0.3, noise_shape=None, seed=None))

#Output layer
model.add(Dense(6,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model_output = model.fit(x_train,y_train,epochs=150,batch_size=20,verbose=1,validation_data=(x_test,y_test),)
model.save(fileOut+'modelSave2')
model.summary()

