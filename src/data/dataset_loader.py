import abc
import tensorflow_datasets as tfds
from .loaded_dataset import LoadedDataset

class ExampleDatasetLoader():
    def __init__(self):
        pass

    def __call__(self, cfg: dict, **kwargs) -> LoadedDataset:
        (ds_train,), ds_info = tfds.load(
            'mnist',
            split=['train'],
            shuffle_files=True,
            as_supervised=True,
            with_info=True,
        )
        return LoadedDataset(ds_train, None)
        