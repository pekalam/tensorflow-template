from model.model import ExampleModel


def model_impl_factory(cfg: dict, **kwargs):
    """Returns model implementation based on config
    """
    if cfg['model'].get('name', None) is None or cfg['model']['name'] == 'example':
        return ExampleModel(cfg)