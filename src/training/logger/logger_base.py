from abc import abstractmethod


class LoggerBase:

    @abstractmethod
    def logger_init(self, cfg: dict):
        pass

    @abstractmethod
    def begin_train_step(self, cfg: dict):
        pass

    @abstractmethod
    def log_metrics(self, result_dict: dict, step):
        pass
    
    @abstractmethod
    def log_model(self, model):
        pass

    @abstractmethod
    def log_end(self):
        pass