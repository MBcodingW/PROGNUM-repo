#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

#Given formula:
def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

#Input values:
A = float(input(f"Input a value for the amplitude A: "))
x0 = float(input(f"Input a value for the the position of the peak x0: "))
sig = float(input(f"Input a value for the width of the peak sigma: "))
z0 = float(input(f"Input a value for the offset in y: "))

#Input of integration limits and integration of the curve:
a = float(input(f"Input a value for the first integration limit a: "))
b = float(input(f"Input a value for the second integration limit b: "))
integral = integrate.quad(gauss, a, b, args=(A, x0, sig, z0))
print(f"The area between x = {a} and x = {b} is {integral}.")
          
#Plotting the curve:
plt.plot(x, y, label='Gaussian curve')
plt.title(rf"Gaussian Function: $f(x) = A e^{{ -\frac{{(x-x_0)^2}}{{2\sigma^2}} }} + z_0$")
plt.fill_between(x, y, where=(x >= a) & (x <= b), color='orange', alpha=0.5,label=f'Integrated Area: {integral[0]:.4f}')
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.legend()
plt.show()

