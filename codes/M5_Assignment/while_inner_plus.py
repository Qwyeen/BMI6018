#!/usr/bin/env python
# coding: utf-8

# In[5]:


def find_innermost_list(input_list):
    while any(isinstance(i,list) for i in input_list):
        for j in input_list:
             if isinstance(j,list):
                  input_list = j
                  break
    return[i+1 for i in input_list]


# In[8]:


input_list = [1,2,3,4,[5,6,7,[8,9]]]
result = find_innermost_list(input_list)
print(result)


# In[ ]:




