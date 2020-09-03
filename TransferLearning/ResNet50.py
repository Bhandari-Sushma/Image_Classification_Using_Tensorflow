import tensorflow as tf
from tensorflow.keras.datasets import cifar10

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

'''
# Import the Model and specify that the model is trained
# inclide_top = False: means we don't want to include the end of the network.
# so we can add our own classifier.
'''
base_model = tf.keras.applications.ResNet50(weights='imagenet', include_top=False)
print(base_model.summary())         # Visualize the base model

# Visualize individual layers
for i, layer in enumerate(base_model.layers):
    print(i, layer.name)

'''
Add new layers at the end of the trained network for new classification problem.
For that first we need to take the output from the trained/base model 
and perform GlobalAveragePooling2D(), which will condense our feature maps from the output
and then we'll add our dense fully connected neural network at the end. 
'''

x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)

# may be we don't need all these extra layers
'''
x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dense(512, activation='relu')(x)
'''

# Here classification on 10 classes from cifer10 data will be done, so 10 neurons are used at the output layer.
preds = tf.keras.layers.Dense(10, activation='softmax')(x)

# final model
model = tf.keras.models.Model(inputs=base_model.input, outputs=preds)
print(model.summary())

# New freeze the layers that are already trained. i.e. layers until 174
for layer in model.layers[:175]:
    layer.trainable = False

for layer in model.layers[175:]:
    layer.trainable = True

input_prepross = tf.keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.resnet50.preprocess_input)


(x_train, y_train), (x_test, y_test) = cifar10.load_data()


model.compile(

    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics=['accuracy'],

)

model.fit(input_prepross.flow(x_train, y_train), batch_size=32, epochs=20)

# Save the entire model as a SavedModel.
print("Saving the model")
model.save('../Saved_Models/TL_ResNet50')


# train the model
print("Evaluating the model: ")
model.evaluate(input_prepross.flow(x_test, y_test))