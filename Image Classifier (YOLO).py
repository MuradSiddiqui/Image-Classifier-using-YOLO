# -*- coding: utf-8 -*-
"""Yolo_(Final) (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ep3MRJ8xs20IapLXNiHIUyaOchDZ9Uw9
"""

# git clone is used for pointing existing storage and make a copy.
!git clone https://github.com/AlexeyAB/darknet

# Commented out IPython magic to ensure Python compatibility.
# darknet change makefile to have GPU and OPENCV enabled
#makefile is special file containing shell cammonds
# %cd darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile #it is used for image processing
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile #Deep Neural Network (cuDNN) is a GPU-accelerated library

# verify CUDA
!/usr/local/cuda/bin/nvcc --version
# make darknet (build)
!make
# get yolov3 pretrained coco dataset weights
!wget https://pjreddie.com/media/files/yolov3.weights

# Commented out IPython magic to ensure Python compatibility.
# define helper functions
def imShow(path):
  import cv2 #this library used for opency
  import matplotlib.pyplot as plt #this is used for visualization
#   %matplotlib inline

  image = cv2.imread(path)
  height, width = image.shape[:2]
  resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off") #Connection refused
  plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
  plt.show()

# use this to upload files
def upload():
  from google.colab import files
  uploaded = files.upload()
  for name, data in uploaded.items():
    with open(name, 'wb') as f:
      f.write(data)
      print ('saved file', name)

# use this to download a file
def download(path):
  from google.colab import files
  files.download(path)

# run darknet detection
!./darknet detect cfg/yolov3.cfg yolov3.weights /content/airport.jpg

# show image using our helper function
imShow('predictions.jpg')

# run darknet detection
!./darknet detect cfg/yolov3.cfg yolov3.weights /content/class.jpg
# show image using our helper function
imShow('predictions.jpg')