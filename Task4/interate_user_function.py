#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
from scipy import integrate

try:
    #Input function:
    #(x**4 * exp((sin(x)+cos(x))))
    user_input = input("Input a function of x: ")
    fun = lambda x: eval(user_input)

    #Integration limits:
    a = eval((input("Input a value for the first integration limit a: ")))
    b = eval((input("Input a value for the second integration limit b: ")))

    #Standard integral calculation
    st_int, error = integrate.quad(fun, a, b)
    print(f"\nUsing standard integration we get: {st_int:.6f}")

    #Monte Carlo integration
    n = 10000
    x_rand = np.random.uniform(a, b, n) 
    y = fun(x_rand)
    mc_int = (b - a) / n * np.sum(y)
    print(f"Using Monte Carlo integration we get: {mc_int:.6f}")

#Possible errors:
except SyntaxError:
    print("\n[Error] Wrong Expression: Check your math syntax.")
except NameError as e:
    print(f"\n[Error] Unknown Function or Variable: {e}")
    print("You can only use the functions 'x', 'sin', 'cos', 'exp', or 'pi'.")

except ValueError:
    print("\n[Error] Invalid Input: The integration limits must be (real) numbers.")

except ZeroDivisionError:
    print("\n[Error] Math Error: The function tried to divide by zero during calculation.")

except Exception as e:
    print(f"\n[Error] An unexpected error occurred: {e}")

