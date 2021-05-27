from omegaconf import DictConfig, OmegaConf
from hydra.experimental import compose, initialize
from omegaconf import OmegaConf
from hydra.core.global_hydra import GlobalHydra



def read_default_config():
    GlobalHydra.instance().clear()
    initialize(config_path="../src/conf")
    cfg = compose(config_name="config")
    return cfg