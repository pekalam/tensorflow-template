from training.early_stopping import EarlyStopping
import pytest

def test_early_stopping_return_values():
    early_stopping = EarlyStopping(2, 0.00001, 2000)
    assert early_stopping.metric_increased == False

    (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == False and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 0 and early_stopping.inc_start_loss == 0
    
    # inc1
    (checkpoint, stop) = early_stopping.add_metric(0.2)
    assert early_stopping.metric_increased == True and stop == False and checkpoint == True and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 1 and early_stopping.inc_start_loss == 0.1

    # should not be counted
    (checkpoint, stop) = early_stopping.add_metric(0.2)
    assert early_stopping.metric_increased == True and stop == False and checkpoint == False and early_stopping.min_delta_iter == 1 and early_stopping.inc_iter == 1 and early_stopping.inc_start_loss == 0.1

    # inc2 - min_delta_iter reset
    (checkpoint, stop) = early_stopping.add_metric(0.3)
    assert early_stopping.metric_increased == True and stop == False and checkpoint == False and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 2 and early_stopping.inc_start_loss == 0.1
    
    # inc3
    (checkpoint, stop) = early_stopping.add_metric(0.4)
    assert early_stopping.metric_increased == True and stop == True and checkpoint == False and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 3 and early_stopping.inc_start_loss == 0.1

    #should throw
    with pytest.raises(ValueError):
        (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == True and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 3 and early_stopping.inc_start_loss == 0.1


def test_early_stopping_stops_when_loss_smaller_than_min_delta_after_min_delta_patience_epochs():
    early_stopping = EarlyStopping(3, 0.01, 2)
    assert early_stopping.metric_increased == False

    (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == False and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 0

    # delta #1
    (checkpoint, stop) = early_stopping.add_metric(0.095)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == False and early_stopping.min_delta_iter == 1 and early_stopping.inc_iter == 0

    # delta #2
    (checkpoint, stop) = early_stopping.add_metric(0.094)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == False and early_stopping.min_delta_iter == 2 and early_stopping.inc_iter == 0   
    
    # delta #3 - should stop and checkpoint
    (checkpoint, stop) = early_stopping.add_metric(0.094)
    assert early_stopping.metric_increased == False and stop == True and checkpoint == True and early_stopping.min_delta_iter == 3 and early_stopping.inc_iter == 0

    #should throw
    with pytest.raises(ValueError):
        (checkpoint, stop) = early_stopping.add_metric(0.094)


def test_early_stopping_when_loss_reach_base_value_returns_checkpoint():
    early_stopping = EarlyStopping(2, 0.00001, 2000)
    assert early_stopping.metric_increased == False

    (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == False and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 0 and early_stopping.inc_start_loss == 0
    
    # inc1
    (checkpoint, stop) = early_stopping.add_metric(0.2)
    assert early_stopping.metric_increased == True and stop == False and checkpoint == True and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 1 and early_stopping.inc_start_loss == 0.1

    # inc2
    (checkpoint, stop) = early_stopping.add_metric(0.3)
    assert early_stopping.metric_increased == True and stop == False and checkpoint == False and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 2 and early_stopping.inc_start_loss == 0.1

    # base val reached
    (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == True and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 0 and early_stopping.inc_start_loss == 0



def test_early_stopping_min_delta_default_params():
    early_stopping = EarlyStopping(2)

    (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == False and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 0 and early_stopping.inc_start_loss == 0

    (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == False and early_stopping.min_delta_iter == 0 and early_stopping.inc_iter == 0 and early_stopping.inc_start_loss == 0