# TODO LIST:

## Scrap for a data:

- [x] Get x-rays images for healthy lungs and with illness
- [x] Prepare labeled directories

## Get the data:

- [x] Use already prepared kaggle's x-ray dataset
## Plot the data:

- [x] Confront healthy lungs with an ill one
 
## Preprocess the data:

- [x] Use openCV library
- [x] Perform image preprocessing and data augmentation

## Build a model class:

- [x] Initialize a neural network model (CNN)
- [x] Perform training and validation
- [x] Use callbacks to stop training if there is no progress
- [x] Log training and validation results
- [x] Perform training and validation
- [x] Perform metrics visualisation
- [x] Tune model to reach better score
- [x] Perform predictions on a test set

## Create an API:

- [ ] Create an endpoint that accepts an image and classifies it as healthy or not
- [ ] Preprocess the image before making a prediction
- [ ] Use celery workers for asynchronous execution
- [ ] Use a database to store uploaded images and add them to the training data
- [ ] Test the API and handle errors

## Containerization:

- [ ] Put everything into a Docker container
