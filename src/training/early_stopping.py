from typing import Tuple


class EarlyStopping:
    def __init__(self, early_stop_patience):
        self.inc_start_loss = 0.
        self.prev_metric_val = float("inf")
        self.inc_iter = 0
        self.early_stop_patience = early_stop_patience
    
    def add_metric(self, metric_val: float) -> Tuple[bool, bool]:
        """[summary]

        Args:
            val_loss (float): [description]

        Returns:
            Tuple[bool, bool]: (should_checkpoint, should_stop)
        """
        should_checkpoint = should_stop = False
        if metric_val >= self.prev_metric_val:
            self.inc_iter += 1
            if self.inc_iter == 1:
                print('Saving checkpoint due to increase of val loss')
                should_checkpoint = True
                self.inc_start_loss = metric_val
            if self.inc_iter > self.early_stop_patience:
                should_stop = True
                print('Stopped due to increase of val loss')

        if self.inc_iter > 1 and metric_val < self.inc_start_loss:
            self.inc_iter = 0
            print('saving checkpoint due to decrease of val loss')
            should_checkpoint = True

        self.prev_metric_val = metric_val
        return (should_checkpoint, should_stop)
    
    @property
    def metric_increased(self) -> bool: 
        return self.inc_iter > 0