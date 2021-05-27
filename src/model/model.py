import tensorflow as tf
from tensorflow.keras.layers import *

class ExampleModel(tf.keras.Model):
    def __init__(self, params: dict = None):
        super(ExampleModel, self).__init__()
        self.classifier = tf.keras.Sequential([
            InputLayer((28,28,1)),
            Reshape((28*28*1,)),
            Dense(50, activation='tanh'),
            Dense(10, activation='softmax'),
        ])

    def call(self, inputs, training=False):
        y = self.classifier(inputs, training=training)
        return y


if __name__ == '__main__':
    model = ExampleModel()
    model.build((1,28,28,1))
    model.summary()