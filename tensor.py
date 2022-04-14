# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("webagg")

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images  = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
			  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
			  metrics=['accuracy'])

try:
	model = tf.keras.models.load_model("trained.model")
except OSError:
	model.fit(train_images, train_labels, epochs = 10)
	model.save('trained.model')

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

probability_model = tf.keras.Sequential([model,
										 tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

print(predictions[0])