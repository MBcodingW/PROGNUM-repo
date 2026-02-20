#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Sirius data
import math
apparentMagnitude = input('Apparent magnitude of Sirius A: ')
absoluteMagnitude = input('Absolute magnitude of Sirius A: ')
#Apparent magnitude Sirius A = -1.46
#Absolute magnitude Sirius A = 1.45

m = float(apparentMagnitude)
M = float(absoluteMagnitude)

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
print(f"The distance to Sirius in lightyears is {d}.")


# In[ ]:




