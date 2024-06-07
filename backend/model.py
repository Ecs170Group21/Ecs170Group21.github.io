import tensorflow as tf

# Load your model (ensure the model file is accessible on your server)
model = tf.keras.models.load_model('path/to/your/model.h5')

def predict(image_path):
    # Code to process the image and make a prediction
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    return predicted_class
