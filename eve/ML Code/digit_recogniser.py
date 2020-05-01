# https://www.youtube.com/watch?v=rml9oBQT8rw

# !/usr/bin/env python
# coding: utf-8
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import model_from_json

from imageprep import *

mnist = tf.keras.datasets.mnist

(training_data, training_labels), (test_data, test_labels) = mnist.load_data()

print(type(test_data))
print(test_data.shape)
print(test_data.dtype)

print(test_data[0].shape)
print(test_data[0][0].shape)

'''
# Printing out first 20 examples from dataset
for i in range(20):
    l = test_data[i].tolist()
    for i in range(28):
        for j in range(28):
            print(l[i][j], end='\t')
        print('')
'''

training_data, test_data = training_data / 255, test_data / 255

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_data, training_labels, epochs=5)

model.evaluate(test_data, test_labels)

predictions = model.predict(test_data)
np.set_printoptions(suppress=True)

print(test_labels[0])
print(predictions[0])

# now attempting to create my own test data
'''
image_data = imageprepare(
    'Path_to_an_image_file')
input_data_2d = get_2d_from_list(image_data, 28, 28)

for i in range(28):
    for j in range(28):
        print(image_data[i*28 + j], end='\t')
    print('')

numpy_array_3d = np.array([input_data_2d], dtype=np.uint8)

print(type(numpy_array_3d))
print(numpy_array_3d.shape)
print(numpy_array_3d.dtype)

numpy_array_3d = numpy_array_3d / 255

prediction = model.predict(numpy_array_3d)
print(prediction)
'''

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")


# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(optimizer=tf.optimizers.Adam(),
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])
'''
prediction = model.predict(numpy_array_3d)
print(prediction)
'''
predictions = model.predict(test_data)
np.set_printoptions(suppress=True)

print(test_labels[0])
print(predictions[0])
