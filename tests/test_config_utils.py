from src.utils.config_utils import get_compatible_config
from omegaconf import DictConfig
from .utils import read_default_config


def test_config_compatibility():
    c1 = DictConfig({'p1': 3, 'runner': {'x': 1}, 'model': {'y_1': 1, 'y_2': 2}, 'training': {}, 'dataset': {}})
    org1 = DictConfig({'p1': 1, 'p2': 2,'runner': {'x': 2}, 'model': {'y_1': 1, 'y_2': 2, 'y_3': 3}, 'training': {}, 'dataset': {}})

    compat1 = get_compatible_config(c1, org1)

    assert compat1.runner.x == c1.runner.x
    assert compat1.model.y_1 == c1.model.y_1 and compat1.model.y_2 == c1.model.y_2 and compat1.model.y_3 == org1.model.y_3
    assert compat1.p1 == 3 and compat1.p2 == 2


def test_default_config_are_valid():
    read_default_config()