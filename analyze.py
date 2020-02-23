import numpy as np
import keras
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence

x_data = np.genfromtxt('mix6mlX.csv',delimiter=',', dtype = (int, int, int, int, int))
y_data = np.genfromtxt('mix6mlY.csv',delimiter=',',dtype=int)
num_classes = np.max(y_data) + 1
tokenizer = Tokenizer(num_words=1000)
x_train = tokenizer.sequences_to_matrix(x_data, mode='binary')
y_train = keras.utils.to_categorical(y_data, num_classes)


model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=1000))
model.add(Dense(units=6, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=32)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

classes = model.predict(x_test, batch_size=128)
