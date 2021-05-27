import tensorflow as tf
import tensorflow.keras as keras
from model.impl_factory import model_impl_factory
from tensorflow.keras.utils import to_categorical
from data.loaded_dataset import LoadedDataset
from training.trainer_base import TrainerBase


class ExampleTrainer(TrainerBase):
    def __init__(self, cfg: dict, dataset_loader = None, model = None, dataset_loader_output: LoadedDataset = None):
        super(ExampleTrainer, self).__init__(cfg, dataset_loader, model, dataset_loader_output)

        self.cfg = cfg
        self.step = tf.Variable(0, dtype=tf.int64)
        self.model = model if model is not None else model_impl_factory(cfg)
        self.optimizer = keras.optimizers.Adam(learning_rate=cfg['training']['learning_rate'])
        self.ds = dataset_loader(cfg) if dataset_loader is not None else dataset_loader_output
        self.loss = keras.losses.CategoricalCrossentropy(from_logits=True)
    

    def _train_step(self):
        num_batches = 0
        total_loss = 0
        for x,y in self.ds.x.take(100).batch(1):
            y = to_categorical(y, 10)
            with tf.GradientTape() as tape:
                y_net = self.model(x, training=True)
                batch_loss = self.loss(y, y_net)
            grads = tape.gradient(batch_loss, self.model.trainable_weights)
            self.optimizer.apply_gradients(zip(grads, self.model.trainable_weights))
            total_loss += batch_loss
            num_batches += 1
        total_loss = total_loss / num_batches
        return total_loss

    def epoch(self) -> dict:
        total_loss = self._train_step()
        self.step.assign_add(1)

        result = {
            'total_loss': total_loss.numpy(),
            'stop': False,
        }

        if self.step == 1:
            result['seed'] = self.seed

        if self.step >= self.cfg['training']['max_iterations']:
            print('Reached max iterations ', self.step.numpy())
            result['stop'] = True

        return result