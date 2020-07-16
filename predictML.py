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


datafile = "testnew"

x_data = pd.read_csv(datafile+"X.csv",names=['s1','s2','s3','s4','s5'])
y_dataR = np.genfromtxt(datafile+"Y.csv",delimiter=',',dtype=int)
num_classes = np.max(y_dataR) + 1
y_data = keras.utils.to_categorical(y_dataR, num_classes)
#x_train, x_test, y_train, y_test = train_test_split(x_data,y_data, test_size=0.20, random_state=0)
x_train = x_data[:880]
x_test = x_data[880:]
y_train = y_data[:880]
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
model.save('modelSave2')
model.summary()

