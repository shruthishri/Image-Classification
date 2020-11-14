# Image-Classification

## Goal

  - Visual Perception of the image dataset using manual
  annotation
  - Implementation of three CNN models to classify and
  label images into classes
  - Analyzing the accuracy of models to conclude their
  performances
  
## Approach

  - Ground Truth is predicted manually
  - Classification of images using VGG16, ResNet50
and MobileNet models
  - Compare the ground truth with the classification of
the models
  - Calculation of top 5 error percentage for all the
three models.

## Results

  - Trained on the same dataset but big difference in
error rate i.e., 4 to 5 times higher error
  - In results, consideration of all objects of the correct
meta class as positive classification

## Conclusion

  - Ambiguous dataset not suited for classification tasks
  - Mistakes due to unknown objects not included in the
training data i.e., No separate class for ‘people’ or ‘human’ but
main focus of many images in the used dataset
  - Multiple objects in picture, some are partly omitted
  - Image size is too large
  - Accurate testing of classification algorithms only
possible with consideration of the trained classes and
by means of a dedicated compiled dataset

