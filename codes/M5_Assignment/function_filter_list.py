#!/usr/bin/env python
# coding: utf-8

# In[8]:


def filter_list(input_list, threshold): 
    output = [x for x in input_list if x <= threshold]
    return output


# In[9]:


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
threshold = 6
result = filter_list(input_list, threshold)
print(result)


# In[ ]:




