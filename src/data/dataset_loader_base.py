import abc
from .loaded_dataset import LoadedDataset

class DataLoaderBase():
    @abc.abstractmethod
    def __call__(self, cfg: dict, **kwargs) -> LoadedDataset:
        pass