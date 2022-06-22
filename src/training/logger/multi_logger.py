


from typing import List
from training.logger.logger_base import LoggerBase


class MultiLogger(LoggerBase):
    def __init__(self, loggers: List[LoggerBase]) -> None:
        self._loggers = loggers

    def begin_train_step(self, cfg: dict):
        for logger in self._loggers:
            logger.begin_train_step()

    def log_metrics(self, result_dict: dict, step):
        for logger in self._loggers:
            logger.log_metrics(result_dict, step)

    def log_end(self):
        for logger in self._loggers:
            logger.log_end()
    
    def logger_init(self, cfg: dict):
        for logger in self._loggers:
            logger.logger_init(cfg)
    
    def log_model(self, model):
        for logger in self._loggers:
            logger.log_model(model)