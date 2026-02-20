#!/usr/bin/env python
# coding: utf-8

# In[18]:


terms = range(101)
sum = 0
list = [0] 
for i in terms:
    print(f"Term {i} in the Fibonnaci sequence is {sum}.")
    if sum == 0:
        sum += 1
        list.append(sum)
    else:
        sum += list[-2]          #Adding up the previous sum to the current sum
        list.append(sum)


# In[ ]:




