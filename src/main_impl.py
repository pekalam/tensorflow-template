from omegaconf import DictConfig, OmegaConf

from runner.default_runner import start_example_training


def main_impl(cfg: DictConfig):
    if cfg.runner.name == 'example':
        start_example_training(cfg)