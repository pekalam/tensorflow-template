from typing import Any
from omegaconf import DictConfig, OmegaConf

from runner.default_runner import start_example_training


def main_impl(cfg: DictConfig, secrets: Any = None):
    if cfg.runner.name == 'example':
        start_example_training(cfg)