# Human Blood Vessel Segmentation Using UNet - Kaggle competition

This repository contains the main notebook used in "SenNet + HOA - Hacking the Human Vasculature in 3D" Kaggle competition. The base architecture used in this notebook is UNet and implemented with Tensorflow. At first it preprocess all images (in competition Kidney scans) and use percentile normalization to emphasize features in the each image. Then converts each image to tensors. It wasn't possible to load the images into tensors at first because Tensorflow do not support .tiff encoding for loading data. Needs to be mentioned some data augmentation added in some versions of the model for better accuracy and TTA.

```python
def percentile_normalize(image, percentile=0.04):
    lower_limit = np.percentile(image, percentile)
    upper_limit = np.percentile(image, 100. - percentile)
    if upper_limit - lower_limit == 0:
        return image
    normalized_image = np.clip(image, lower_limit, upper_limit)
    normalized_image = (normalized_image - lower_limit) / (upper_limit - lower_limit)
    return normalized_image
```

After all, there is a class that is a wrapper for the model. Iterative learning used to reach better accuracy and prevent corruptions during training process by implementing checkpoint scheduler. Different type of loss functions implemented to checkthe best fit for the problem (dice coef loss, binary corssentropy, both).

```python
class SentimentSegmentation():

    def __init__(self, x, y, val_x, val_y, input_shape=(SIZE,SIZE,1), encoders=None, decoders=None):
        self.seed = 2024
        self.encoders = encoders
        self.decoders = decoders
        self.x_train = x
        self.y_train = y
        self.x_test = val_x
        self.y_test = val_y
        self.input_shape = input_shape
        self.early_stopping = EarlyStopping(monitor='val_loss', patience=10, verbose=1)
        self.generate()
        self.gpus = tf.config.experimental.list_physical_devices('GPU')
        self.checkpoint_path = "/kaggle/working/model_checkpoint.ckpt"
        self.model_checkpoint = ModelCheckpoint(self.checkpoint_path, monitor='val_loss', verbose=1, save_best_only=False)
    ...
    
```