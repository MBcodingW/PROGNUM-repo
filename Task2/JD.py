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


# In[1]:


#Extension and correction of code above
#Input of variables for first Julian date:
Y1 = float(input(f"Input the year: "))
M1 = float(input(f"Input the month: "))
D1 = float(input(f"Input the day: "))

# Setting all devision terms to be seperate formulas for clarity.
x1 = (M1+9)//12
x2 = 7*(Y1+x1)//4
x3 = (M1-9)//7
x4 = (Y1+x3)//100
x5 = 3*(x4 + 1)//4
x6 = (275*M1)//9

# The JD formula becomes:
JD1 = 367*Y1 - x2 - x5 + x6 + D1 + 1721029-0.5


#Input of variables for second Julian data:
Y2 = float(input(f"Input the year: "))
M2 = float(input(f"Input the month: "))
D2 = float(input(f"Input the day: "))

# Setting all devision terms to be seperate formulas for clarity.
x1 = (M2+9)//12
x2 = 7*(Y2+x1)//4
x3 = (M2-9)//7
x4 = (Y2+x3)//100
x5 = 3*(x4 + 1)//4
x6 = (275*M2)//9

# The JD formula becomes:
JD2 = 367*Y2 - x2 - x5 + x6 + D2 + 1721029-0.5

#number of days between two dates:
Days = abs(JD2-JD1)

#I was born on the 13th of June 2008. As of correcting this script, the date is 28-2-2026.
print(f"My age expressed in days: {Days}.")


# In[ ]:




