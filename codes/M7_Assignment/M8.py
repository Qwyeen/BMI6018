#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1
import numpy as np
print(np.__version__)


# In[5]:


# 2
arr = np.arange(10)
print(arr)


# In[7]:


# 3
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_data = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')


# In[9]:


iris_data[:5]


# In[23]:


# 4
position = -1
for i in iris_data:
    position += 1
    if i[3] > 1:
        break
print('Position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset: {}'.format(position))


# In[24]:


# 5
np.random.seed(100)
a = np.random.uniform(1,50, 20)


# In[27]:


a[a > 30] = 30
a[a < 10] = 10


# In[29]:


print(a)


# In[ ]:




