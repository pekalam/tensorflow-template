import tensorflow as tf
from data.loaded_dataset import LoadedDataset

class TrainerBase():
    def __init__(self, cfg: dict, dataset_loader = None, model = None, dataset_loader_output: LoadedDataset = None):
        assert cfg is not None
        assert (dataset_loader is not None) ^ (dataset_loader_output is not None)
        assert (cfg is not None) or (model is not None)
        
        if cfg['training']['seed'] is not None:
            tf.random.set_seed(cfg['training']['seed'])
            self.seed = cfg['training']['seed']
        else:
            self.seed = None