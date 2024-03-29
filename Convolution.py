AIM: Write a python program on convolutional neural network to classify images from any standard datasets in the public domain using Keras framework

PROGRAM

import matplotlib

from matplotlib import pyplot as plt

import numpy as np

import matplotlib

import matplotlib.pyplot as plt

from keras.datasets import fashion_mnist
(train_X ,train_Y), (test_X,test_Y) = fashion_mnist.load_data() 
from keras.utils.np_utils import to_categorical 
%matplotlib inline

print ('training data shape: ', train_X.shape, train_Y.shape)

print ('testing data shape: ', test_X.shape, test_Y.shape)

('Training data shape:',(60000, 28, 28), (60000, ))

('Testing data shape:',(10000, 28, 28), (10000, ))

classes = np.unique(train_Y)

nClasses = len(classes)

print('total number of outputs: ', nClasses)

print('output classes: ', classes)
