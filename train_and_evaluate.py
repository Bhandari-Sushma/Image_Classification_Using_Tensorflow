from Net import *
from tensorflow.keras.datasets import cifar10


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# import data

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print("Training the model: ")
model.fit(x_train, y_train, epochs=5)

# Save the entire model as a SavedModel.

model.save('saved_model/my_model')

print("Evaluating the model: ")
model.evaluate(x_test, y_test)


