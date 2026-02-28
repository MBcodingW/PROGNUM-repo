#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import exp
from matplotlib import pyplot as plt

#Values
x = range(-5, 6)
y = []
for p in x:
    func = (exp(p)+exp(-p))/2
    y.append(func)

#Plot
plt.plot(x, y, marker='o', color='r', label="Data")
plt.title(r"Catenary function")
plt.grid()
plt.ylabel(r"Height (m)")
plt.xlabel(r"x (m)")
plt.legend()
plt.show()

# In[ ]:




