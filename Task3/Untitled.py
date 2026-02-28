#!/usr/bin/env python
# coding: utf-8

# In[1]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
M_moon = 7.35e22
stm = []
for m in masses:
    if m <= M_moon:
        stm.append(m)
print(stm)

slice_m = masses[slice(-5, None, None)]
print(slice_m)

avg = sum(slice_m)/len(slice_m)
print(avg)


# In[ ]:




