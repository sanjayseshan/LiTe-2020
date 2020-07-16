#!/usr/bin/python3
import socket
#import serial
import time
import sys

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

gestures=["generic"]

print("delta Time, Unix Time, pr1, pr2, pr3, pr4, pr5, label")
f.write("delta Time, Unix Time, pr1, pr2, pr3, pr4, pr5, label\n")
trel = time.time()
print(trel)
for gesture in gestures:
    continueQ = input("Do "+gesture+"? [Y/n]: ")
    if continueQ == "y" or continueQ == "" or continueQ == "Y":
        getData(99999999999999999999999999999999999, gesture)
#            while True:
#                    print(getSerialBuf().split(","))
    elif continueQ == "n" or continueQ == "N":
        continueQ = "n"
    
f.close()
