import tensorflow as tf
from tensorflow.keras.models import save_model, Sequential

model_path = 'model2-002.model'
model = tf.keras.models.load_model(model_path)
save_model(model,model_path + r'model-010.h5', save_format='h5')
