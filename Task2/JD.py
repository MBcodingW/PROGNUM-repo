#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Input of variables
Y = float(input(f"Input the year: "))
M = float(input(f"Input the month: "))
D = float(input(f"Input the day: "))

# Setting all devision terms to be seperate formulas for clarity.
x1 = (M+9)//12
x2 = 7*(Y+x1)//4
x3 = (M-9)//7
x4 = (Y+x3)//100
x5 = 3*(x4 + 1)//4
x6 = (275*M)//9

# The JD formula becomes:
JD = 367*Y - x2 - x5 + x6 + D + 1721029-0.5

#JD
print(f"The Julian data is: {JD}.")


# In[ ]:




