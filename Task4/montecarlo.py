#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as  np
from numpy import sin, cos, tan, log, log10 

a = float(input("Input a starting value: "))
b = float(input("Input an ending value: "))
n = int(input("Input amount of random input: "))

x = np.random.uniform(a, b, n) 
fun = input("Enter a function f(x) = ")
y = eval(fun)

integral = (b-a)/n * np.sum(y)

print(integral)


# In[ ]:




