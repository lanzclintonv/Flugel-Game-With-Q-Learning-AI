import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

dataset = np.load("training_data_vel.npy")

print(len(dataset))
train = dataset[-245000:]
test = dataset[:-245000]

x_train = np.array([i[0] for i in train])
y_train = np.array([i[1] for i in train])
x_test = np.array([i[0] for i in test])
y_test = np.array([i[1] for i in test])



model2 = Sequential()
model2.add(Dense(3,input_shape = (3,), activation = 'relu'))
model2.add(Dense(8,activation = 'relu'))
model2.add(Dense(8, activation = 'relu'))
model2.add(Dense(1,activation = 'relu'))
model2.compile(loss = 'mean_squared_error', optimizer = 'sgd', metrics = ['accuracy'])
model2.fit(x = x_train, y = y_train, epochs = 1000,batch_size = 10, shuffle = True, validation_data = (x_test, y_test),verbose = 2)

model2.save("test_model_v1.h5")
