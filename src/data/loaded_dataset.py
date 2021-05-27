import tensorflow as tf

class LoadedDataset():
    """Contains dataset loaded by calling DatasetLoader object __call__ method
    """
    def __init__(self, x, y, x_val = None, y_val = None, x_test = None, y_test = None):
        self._x = x
        self._y = y
        self._x_val = x_val
        self._y_val = y_val
        self._x_test = x_test
        self._y_test = y_test

    @property
    def x(self) -> tf.data.Dataset: return self._x

    @property
    def y(self) -> tf.data.Dataset: return self._y

    @property
    def x_val(self) -> tf.data.Dataset: return self._x_val

    @property
    def y_val(self) -> tf.data.Dataset: return self._y_val

    @property
    def x_test(self) -> tf.data.Dataset: return self._x_test
    
    @property
    def y_test(self) -> tf.data.Dataset: return self._y_test