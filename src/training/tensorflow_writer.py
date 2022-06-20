
import os
import tensorflow as tf

class TensorflowWriter:
    __instance = None

    @staticmethod
    def get_instance(logdir: str):
        if TensorflowWriter.__instance is not None:
            return TensorflowWriter.__instance
        
        if not os.path.exists(logdir):
            print('Creating logdir directory %s' % logdir)
            os.mkdir(logdir)
        TensorflowWriter.__instance = tf.summary.create_file_writer(logdir)
        return TensorflowWriter.__instance

