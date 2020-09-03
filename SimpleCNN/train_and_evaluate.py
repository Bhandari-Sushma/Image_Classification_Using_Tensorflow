from SimpleCNN.Net import *
from tensorflow.keras.datasets import cifar10

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# import data -> cifar10 dataset is used

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# train the model
print("Training the model: ")
model.fit(x_train, y_train, batch_size=32, epochs=20)

# Save the entire model as a SavedModel.
print("Saving the model")
model.save('../Saved_Models/Net')


# train the model
print("Evaluating the model: ")
model.evaluate(x_test, y_test)
