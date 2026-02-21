#!/usr/bin/env python
# coding: utf-8

# In[10]:


#The given formula:
print(f"The given formula is in the form: f(x) = ax\u00b2 + bx +c = 0.")

#Inputs for abc
a = float(input(f" a = "))
b = float(input(f" b = "))
c = float(input(f" c = "))

#The formula becomes
print(f"The inputted values give the formula: f(x) = {a}x\u00b2 + {b}x +{c} = 0.")

#Import the square root function from the math library
from math import sqrt

#Checking amount of solutions and calculating solutions using conditions
D = b**2 -4*a*c
if D < 0:
    print(f"D = {D} < 0, therefore this equation does not have a real solution.")
elif D ==0:
    x = -b/(2*a)
    print(f"D = {D}, therefore the solution for this equation is x = {x}.")
else:
    x1 = (-b+sqrt(D))/(2*a)
    x2 = (-b-sqrt(D))/(2*a)
    print(f"D = {D} > 0, the two solutions to this equation are x1 = {x1} and x2 = {x2}.")


# In[ ]:




