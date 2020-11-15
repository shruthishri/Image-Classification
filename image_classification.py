import keras
import numpy as np
from keras.applications import vgg16, inception_v3, resnet50, mobilenet

# Load the VGG model
vgg_model = vgg16.VGG16(weights='imagenet')

# Load the Inception_V3 model
inception_model = inception_v3.InceptionV3(weights='imagenet')

# Load the ResNet50 model
resnet_model = resnet50.ResNet50(weights='imagenet')

# Load the MobileNet model
mobilenet_model = mobilenet.MobileNet(weights='imagenet')

#Loading the pre trained images

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

filename= '/home/shruthi/Downloads/avt_image_db_selection/3LMlKF8J.png'
# load an image in PIL format
original = load_img(filename, target_size=(224, 224))
print('PIL image size', original.size)
plt.imshow(original)
plt.show()

# convert the PIL image to a numpy array
# IN PIL - image is in (width, height, channel)
# In Numpy - image is in (height, width, channel)
numpy_image = img_to_array(original)
plt.imshow(np.uint8(numpy_image))
plt.show()
print('numpy array size', numpy_image.shape)

# Convert the image / images into batch format
# expand_dims will add an extra dimension to the data at a particular axis
# We want the input matrix to the network to be of the form (batchsize, height, width, channels)
# Thus we add the extra dimension to the axis 0.
image_batch = np.expand_dims(numpy_image, axis=0)
print('image batch size', image_batch.shape)
plt.imshow(np.uint8(image_batch[0]))

#Perdicting the image

# prepare the image for the VGG model
#processed_image = vgg16.preprocess_input(image_batch.copy())

# get the predicted probabilities for each class
#predictions = vgg_model.predict(processed_image)
# print predictions

# prepare the image for the mobilenet model
#processed_image = mobilenet.preprocess_input(image_batch.copy())

# get the predicted probabilities for each class
#predictions = mobilenet_model.predict(processed_image)
# print predictions

# prepare the image for the resnet50 model
processed_image = resnet50.preprocess_input(image_batch.copy())

# get the predicted probabilities for each class
predictions = resnet_model.predict(processed_image)
# print predictions




# convert the probabilities to class labels
# We will get top 5 predictions which is the default
label = decode_predictions(predictions)
print(label)



