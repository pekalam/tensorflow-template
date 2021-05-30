import tensorflow as tf
from data.loaded_dataset import LoadedDataset
import time
import numpy as np

class TrainerBase():
    def __init__(self, cfg: dict, dataset_loader = None, model = None, dataset_loader_output: LoadedDataset = None):
        assert cfg is not None
        assert (dataset_loader is not None) ^ (dataset_loader_output is not None)
        assert (cfg is not None) or (model is not None)
        
        if cfg['training']['seed'] is None:
            self.seed = cfg['training']['seed'] = int(time.time())
            print('generated new seed new seed ', self.seed)
        else:
            self.seed = cfg['training']['seed']
            print('seed read from cfg ', self.seed)
        tf.random.set_seed(self.seed)
        np.random.seed(seed=self.seed)