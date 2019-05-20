
# All code is learned / refer from youtube channgel, 大數據軟體

#!/usr/bin/env python
# coding: utf-8

# In[3]:


# got some difficult to load this..
# check this thread to solve : https://github.com/numpy/numpy/issues/12977

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


# In[4]:


# init the CNN
classifier = Sequential()

# Convolution, 32 feather map, each is 3 x 3, input shape shall be the same as your img shape
classifier.add(Conv2D(32, (3,3), input_shape = (64,64,3), activation = 'relu'))


# In[5]:


# max pooling, handle noice
classifier.add(MaxPooling2D(pool_size = (2,2)))


# In[6]:


# another layer of Convolution and pooling
classifier.add(Conv2D(32, (3,3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))


# In[7]:


# flattening , to one-dim vector
classifier.add(Flatten())


# In[8]:


# Fully Connected: use 128 neuro
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 3, activation = 'softmax'))  # 3 category

# choose the optimizer
classifier.compile(optimizer = 'adam', 
                   loss = 'categorical_crossentropy', 
                   metrics = ['accuracy'])


# In[9]:


## use keras to access our data

from keras.preprocessing.image import ImageDataGenerator

# standardlize, shift...
train_datagen = ImageDataGenerator(rescale = 1./255, 
                                   shear_range = 0.2, 
                                   zoom_range = 0.2, 
                                   horizontal_flip = True)


# In[10]:


test_datagen = ImageDataGenerator(rescale = 1./255)


# In[11]:


# set up the trasining set and test set
training_set = train_datagen.flow_from_directory('train/', 
                                                 target_size = (64,64), 
                                                 batch_size = 10, 
                                                 class_mode = 'categorical')


# In[12]:


test_set = train_datagen.flow_from_directory('test/',
                                             target_size = (64,64), 
                                             batch_size = 10, 
                                             class_mode = 'categorical')


# In[17]:


# Build Model

history = classifier.fit_generator(training_set,
                                   nb_epoch = 30,
                                   nb_val_samples = 10,
                                   steps_per_epoch = 30,
                                   verbose = 1,
                                   validation_data = test_set
                                   )


# In[18]:


# take some image to show our result

from PIL import Image
im = Image.open('img_predict.jpg')
im


# In[52]:


# also use CV to get the face parameters
# note: we found out only got 5 out of 6 faces

from PIL import Image
import cv2 as cv
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv.imread('img_predict.jpg')
faces = face_cascade.detectMultiScale(img, 1.2, 3)
faces


# In[30]:


# use this tansform to convert 0,1,2 to name

transform_dic = {
    'cheng': 'Janine, Cheng',
    'yui':'Aragaki, Yui',
    'zhou':'Tracy, Chou'
}

name_dic = {v:transform_dic.get(k) for k,v in training_set.class_indices.items() }
name_dic


# In[56]:


from keras.preprocessing import image
import numpy as np
from matplotlib import pyplot as plt

font = cv.FONT_HERSHEY_PLAIN

for x,y,w,h in faces:
    box = (x, y, w+x, y+h)
    crpimg = im.crop(box).resize((64,64)) # crop above 6 combined pic and resize to same size
    target_image = image.img_to_array(crpimg)  # transfer to array
    target_image = np.expand_dims(target_image, axis = 0) # add one-dim for keras
    
    # use model to predict
    res = classifier.predict_classes(target_image)[0] # result is a label
    
    # use cv to add rectangle and name
    cv.rectangle(img,(x,y),(x+w,y+h),(14,201,155),2)
    cv.putText(img, name_dic.get(res), (x + int(w/3)-70, y-10), font, 1.5,(14,201,255),3)
    


# In[58]:


# show the image

get_ipython().run_line_magic('pylab', 'inline')
plt.figure(figsize=(20,20))
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

