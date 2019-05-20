# All code is learned / refer from youtube channgel, 大數據軟體


#!/usr/bin/env python
# coding: utf-8

# # Get google Imgae

# In[38]:


# the url used below need to go thru the network to find the start parameter...
# it's not the one in your url bar

url = 'https://www.google.com/search?ei=VbmpXLzHN4qNr7wPirGV6AQ&yv=3&q=%E5%BC%B5%E9%88%9E%E7%94%AF&tbm=isch&vet=10ahUKEwj8xfzBzL3hAhWKxosBHYpYBU0QuT0IbigB.VbmpXLzHN4qNr7wPirGV6AQ.i&ved=0ahUKEwj8xfzBzL3hAhWKxosBHYpYBU0QuT0IbigB&ijn=1&start=300&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc'
# https://www.youtube.com/watch?v=B0d6PpjWQ-Q

import requests


res = requests.get(url)

# res.text


# In[39]:


# Note: the tutorial's code doesn't work to get all 100 pictue in the page
# The google change src attribute name...so you need to check html inside to find out this different..


from bs4 import BeautifulSoup

# get the response txt foramt and parse it with lxml parser
soup = BeautifulSoup(res.text, 'lxml')

# use select to select tag
count = 0 # for double check how many iteration it goes
for i in soup.select('img'):
    count+=1
    if i.get('src'):
        print(i.get('src'))
    else:
        print(i.get('data-src'))
print(count)


# In[7]:


# write pic file into 1.jpg file

with open('1.jpg', 'wb') as f:
    res = requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMaNMTeVW7woctQtn1YduD0yzh0i2dNGCSPvXAvqySVuS18_WCFs-s-u0")
    f.write(res.content)


# In[8]:


# Use Pillow to show image

from PIL import Image
Image.open('1.jpg')


# In[16]:


import requests
import bs4 import BeautifulSoup

data_url = "https://www.google.com/search?ei=VbmpXLzHN4qNr7wPirGV6AQ&yv=3&q={}&tbm=isch&vet=10ahUKEwj8xfzBzL3hAhWKxosBHYpYBU0QuT0IbigB.VbmpXLzHN4qNr7wPirGV6AQ.i&ved=0ahUKEwj8xfzBzL3hAhWKxosBHYpYBU0QuT0IbigB&ijn=1&start={}&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc"

def getIdolImg(keyword, dst_path):

     ## use requests to send req, go thru 3 iteration, requesr url change from 100 to 300
    for i in range(3): 
        res = requests.get(data_url.format(keyword, i * 100))
        
        # use bf4 to parse and get img url and define file name
        soup = BeautifulSoup(res.text, 'lxml')
        
        for elt in soup.select('img'):
            if elt.get('src'):
                img_url = elt.get('src')
            else:
                img_url = elt.get('data-src')
            
            file_name = img_url.split('tbn:')[1]
            
            # write image into file and also define the file name within created dir
            with open(dst_path + file_name + '.jpg', 'wb') as f:
                res2 = requests.get(img_url)
                f.write(res2.content)
            


# In[5]:


## create dir
# import os
# os.mkdir('idol_cheng/')
# os.mkdir('idol_zhou/')
# os.mkdir('idol_yui')


# In[20]:


import requests
from bs4 import BeautifulSoup

getIdolImg('張鈞甯','idol_cheng/')
getIdolImg('周采詩','idol_zhou/')
getIdolImg('新垣結衣','idol_yui/')

