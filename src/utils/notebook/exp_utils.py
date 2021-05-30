from hydra.experimental import compose, initialize_config_dir
from hydra.core.global_hydra import GlobalHydra
from omegaconf import DictConfig, OmegaConf
import os
from utils.config_utils import save_as_one_file

def load_exp_config(branch, name, local_logdir = False):
    GlobalHydra.instance().clear()
    config_dir = os.path.join(os.path.sep.join(os.getcwd().split(os.path.sep)[0:-1]), "experiments", branch, name)
    print('config_dir: ', config_dir)
    with initialize_config_dir(config_dir):
        cfg = compose(config_name="config")
    os.makedirs('../jupyter-outputs/.hydra', exist_ok=True)
    if local_logdir:
        if cfg.runner.name == 'ray':
            cfg.runner.mlflow.tracking_uri = '../jupyter-outputs/mlflow'
            cfg.runner.run.local_dir = '../jupyter-outputs/ray_results'
    if os.path.exists('../jupyter-outputs/.hydra/config.yaml'):
        os.remove('../jupyter-outputs/.hydra/config.yaml')
    save_as_one_file(cfg, '../jupyter-outputs/.hydra/config.yaml')
    return cfg

def pretty_print_cfg(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))