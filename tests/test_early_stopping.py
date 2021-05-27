from training.early_stopping import EarlyStopping

def test_early_stopping_return_values():
    early_stopping = EarlyStopping(3)
    assert early_stopping.metric_increased == False

    (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == False
    
    (checkpoint, stop) = early_stopping.add_metric(0.2)
    assert early_stopping.metric_increased == True and stop == False and checkpoint == True

    (checkpoint, stop) = early_stopping.add_metric(0.2)
    assert early_stopping.metric_increased == True and stop == False and checkpoint == False

    (checkpoint, stop) = early_stopping.add_metric(0.1)
    assert early_stopping.metric_increased == False and stop == False and checkpoint == True

    (checkpoint, stop) = early_stopping.add_metric(0.2)
    assert early_stopping.metric_increased == True and stop == False and checkpoint == True

