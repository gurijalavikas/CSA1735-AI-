import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Example dataset (XOR function)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Define the model
model = keras.Sequential([
    layers.Dense(2, input_shape=(2,), activation='relu'),  # Hidden layer with 2 neurons
    layers.Dense(1, activation='sigmoid')  # Output layer with 1 neuron (sigmoid for binary classification)
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, verbose=1)

# Predict
predictions = model.predict(X)
print(predictions)
