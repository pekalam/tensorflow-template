import hydra
from omegaconf import DictConfig, OmegaConf
from utils.config_utils import get_compatible_config
from hydra.experimental import compose, initialize, initialize_config_dir
import sys
from main_impl import main_impl 

org_cfg = None


def _load_org_config(model=None):
    global org_cfg
    with initialize(config_path='conf'):
        org_cfg = compose(config_name="config", overrides=['model='+model] if model is not None else [])
        OmegaConf.set_struct(org_cfg, True)


def _load_cfg_from_argv():
    custom_path = [a.split('=')[1] for a in sys.argv if '--config-path' in a]
    model = None
    if len(custom_path) > 0:
        with initialize(config_path=custom_path[0]):
            cfg = compose(config_name="config")
            OmegaConf.set_struct(cfg, True)
            model = cfg.model.name
    absoulute_config_path = [a.split('=')[1] for a in sys.argv if '--absoulute-config-path' in a]
    absolute_config = None
    if len(absoulute_config_path) > 0:
        with initialize_config_dir(config_dir=absoulute_config_path[0]):
            absolute_config = compose(config_name="config")
            model = absolute_config.model.name
    return (absolute_config, model)


@hydra.main(config_name='config', config_path='conf')
def main(cfg: DictConfig) -> None:
    global org_cfg
    cfg = get_compatible_config(cfg, org=org_cfg)
    print(OmegaConf.to_yaml(cfg))
    main_impl(cfg)


def notebook_main(cfg: DictConfig):
    _load_org_config(cfg.model.name)
    main(cfg)

if __name__ == '__main__':
    (absolute_config, model) = _load_cfg_from_argv()
    _load_org_config(model)
    if absolute_config is not None:
        main(absolute_config)
    else:
        main()
