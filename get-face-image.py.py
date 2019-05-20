# All code is learned / refer from youtube channgel, 大數據軟體

#!/usr/bin/env python
# coding: utf-8

# In[3]:


## create dir
# import os
# os.mkdir('idol_cheng/')
# os.mkdir('idol_zhou/')
# os.mkdir('idol_yui')

import os
os.listdir('idol_cheng')[0:8]


# In[15]:


from PIL import Image
img = Image.open('idol_cheng/ANd9GcQ3haFFZ8O3R3KU_Yzyl6bHK4I8yvS-MoCdc5YXUp7yPtc3yXZQVg.jpg')
img


# In[7]:


import cv2 as cv
imgary = cv.imread('idol_cheng/ANd9GcQ3haFFZ8O3R3KU_Yzyl6bHK4I8yvS-MoCdc5YXUp7yPtc3yXZQVg.jpg')
# imgary
imgary.shape


# In[9]:


# use CV function to identify face in the picture
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(imgary,1.3,5)  # generate a list, possible have mutiple faces


# In[11]:


# get the face of 4 para(x,y,w,h), this ex only have one face
faces


# In[10]:


# unpack w,y,w,h
x,y,w,h = faces[0]


# In[16]:


# use PIL to crop and resize
crop_img = img.crop((x,y,x+w, y+h)).resize((64,64))
crop_img


# In[19]:


import os
os.mkdir('idol_cheng_face')
os.mkdir('idol_zhou_face')
os.mkdir('idol_yui_face')


# In[22]:


# os.mkdir('idol_cheng/')
# os.mkdir('idol_zhou/')
# os.mkdir('idol_yui')

import os
src_path = 'idol_yui/'
dst_path = 'idol_yui_face/'
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

for file_name in os.listdir(src_path):
    img = Image.open(src_path + file_name) # save img from path + file name
    
    # use cv to get the face x,y,w,h
    imgary = cv.imread(src_path + file_name)
    faces = face_cascade.detectMultiScale(imgary,1.3,5)
    
    if len(faces) == 1:   # exclude over 1 face in the pic
        x,y,w,h = faces[0]
        crop_img = img.crop((x,y,x+w, y+h)).resize((64,64))  # corp image
        crop_img.save(dst_path + file_name)


# In[ ]:




