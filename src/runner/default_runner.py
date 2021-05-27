from omegaconf import dictconfig
from data.dataset_loader import ExampleDatasetLoader
from model.impl_factory import model_impl_factory
from training.trainer import ExampleTrainer

def start_example_training(cfg: dictconfig):
    model = model_impl_factory(cfg)
    dataset_loader = ExampleDatasetLoader()
    trainer = ExampleTrainer(cfg, model=model, dataset_loader=dataset_loader)

    result = trainer.epoch()
    while result['stop'] == False:
        print(result)
        result = trainer.epoch()
    