

# NCCU 機器學習課程


#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


from sklearn.datasets import load_iris
iris = load_iris()
print(iris.DESCR)


# In[13]:


X = iris.data
Y = iris.target

print(X[0])
X = X[:,2:]  # 拿後面兩個，花瓣的長寬來predict


# In[11]:


# Y


# In[9]:


# 分成訓練和驗證資料集
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =  train_test_split(X,Y,
                                                     test_size = 0.2, 
                                                     random_state =87)


# In[14]:


# 看一下要訓練的資料
# 用顏色去區分種類
plt.scatter(x_train[:,0], x_train[:,1], c=y_train)


# In[16]:


# 進行學習
from sklearn.svm import SVC
clf = SVC()
clf.fit(x_train, y_train)


# In[18]:


# 訓練結束，進行預測
y_predict = clf.predict(x_test)

# 相減，用顏色來區分預測和驗證的差異
plt.scatter(x_test[:,0], x_test[:,1], c=y_predict-y_test)


# # 更炫的畫圖法

# In[21]:


# arange, 類似range
np.arange(0.3,10.2,0.2)


# In[24]:


## 建立格點
x1, x2 = np.meshgrid(np.arange(0,7,0.02), np.arange(0,3,0.02))
x1


# In[23]:


# 進行預測

#但是..拉平後如果是這樣...
xx = [1,2,3,4]
yy = [5,6,7,8]

#需要變成這樣 [[1,5],[2,6]]
#用這個.c_去轉, 類似python 的zip
np.c_[xx,yy]


# In[25]:


# 先把x1, x2 拉平再zip
Z = clf.predict(np.c_[x1.ravel(),x2.ravel()])


# In[27]:


# 需要轉一下 Z 才好畫圖
# 進行數據分析，其實資料就要一直轉換到適用的。
Z = Z.reshape(x1.shape)
plt.contourf(x1,x2,Z,cmap=plt.cm.coolwarm,alpha=0.8)
plt.scatter(X[:,0], X[:,1],c=Y)

