#!/usr/bin/python

import serial
import time
import sys

# Determine the file to save data to and Arduino port
fileOut = sys.argv[2]
port = sys.argv[1]

f = open(fileOut, "w")

# Open Arduino serial
ser = serial.Serial(port, 9600, timeout=1)
def getData(timeout, label):
    # measure delta time of a single gesture cycle for timeout
    timeI = time.time()
    while time.time()-timeI < timeout:
        try:
            reading = ser.readline() # Read sensor values from Arduino
            # Record delta Time, Unix time, ldr readings, and label to a file
            data = [0,0,0,0,0,0,0,""]
            data[0] = time.time()-timeIA
            data[1] = time.time()
            data[2] = int(reading.split('\n')[0].split(",")[0])
            data[3] = int(reading.split('\n')[0].split(",")[1])
            data[4] = int(reading.split('\n')[0].split(",")[2])
            data[5] = int(reading.split('\n')[0].split(",")[3])
            data[6] = int(reading.split('\n')[0].split(",")[4])
            data[7] = label
            for i in data:
                print str(i)+",",
                f.write(str(i)+",")
            print ""
            f.write("\n")
        except:
            pass

gestures = ["extend","fist","one"]*2 # declare labels of which gestrues are being tested

print("delta Time, Unix Time, pr1, pr2, pr3, pr4, pr5, label") # file headers
f.write("delta Time, Unix Time, pr1, pr2, pr3, pr4, pr5, label\n")

# Collect data for each gesture cycle for 5.0s
timeIA = time.time()
for gesture in gestures:
    continueQ = raw_input("Do "+gesture+"? [Y/n]: ")
    if continueQ == "y" or continueQ == "" or continueQ == "Y":
        getData(5.0, gesture)
    elif continueQ == "n" or continueQ == "N":
        continueQ = "n"
    
f.close()
