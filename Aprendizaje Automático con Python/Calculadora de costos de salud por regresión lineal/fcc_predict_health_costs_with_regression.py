# Commented out IPython magic to ensure Python compatibility.
# Import libraries. You may or may not use all of these.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

# Print Callback f(x)
class EpochDots(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 50 == 0:
      print()
      print('Epoch: {:d}, '.format(epoch), end='')
      for name, value in sorted(logs.items()):
        print('{}:{:0.4f}'.format(name, value), end=', ')
      print()

    print('.', end='')

# Import data
dataset = pd.read_csv('insurance.csv')
dataset.tail()

# Change categorical to numeric
dataset['sex'].replace(['male', 'female'], [0, 1], inplace=True)
dataset['smoker'].replace(['yes', 'no'], [1, 0], inplace=True)
dataset['region'].replace(['southwest', 'southeast', 'northwest', 'northeast'], [1, 2, 3, 4], inplace=True)
dataset.head()

# Pop off expenses
df_train = dataset.sample(frac=0.8, random_state=0)
train_labels = df_train['expenses']
train_dataset = df_train.drop('expenses', axis=1)

df_test = dataset.drop(df_train.index)
test_labels = df_test['expenses']
test_dataset = df_test.drop('expenses', axis=1)

# Build sequential model
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(len(train_dataset.keys()),)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer= tf.keras.optimizers.RMSprop(0.05),
    loss='mse',
    metrics=['mae', 'mse']
)

model.summary()

# Fit model
r = model.fit(train_dataset, train_labels, epochs=500,
              verbose=0, callbacks=[EpochDots()])

# Evaluate model
res = model.evaluate(test_dataset, test_labels, verbose=2)
print(res) 

# RUN THIS CELL TO TEST YOUR MODEL. DO NOT MODIFY CONTENTS.
# Test model by checking how well the model generalizes using the test set.
loss, mae, mse = model.evaluate(test_dataset, test_labels, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} expenses".format(mae))

if mae < 3500:
  print("You passed the challenge. Great job!")
else:
  print("The Mean Abs Error must be less than 3500. Keep trying.")

# Plot predictions.
test_predictions = model.predict(test_dataset).flatten()

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True values (expenses)')
plt.ylabel('Predictions (expenses)')
lims = [0, 50000]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims,lims)