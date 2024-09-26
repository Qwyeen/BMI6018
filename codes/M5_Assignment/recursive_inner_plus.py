#!/usr/bin/env python
# coding: utf-8

# In[2]:


def recur_innermost_plus(input_list):
    # if there is no nested list
    if all(not isinstance(i, list) for i in input_list):
        return [x + 1 for x in input_list]
    
    for i in input_list:
        if isinstance(i, list):
            return recur_innermost_plus(i)


# In[4]:


input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9]]]
result = recur_innermost_plus(input_list)
print(result)


# In[ ]:




