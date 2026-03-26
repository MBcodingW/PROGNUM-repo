#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Fibonacci:
    
    def nthterm(self, N):
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a + b
        return a
    def divisiblebym(self, N, M):
        a, b = 0, 1
        n = self.nthterm(N)
        results = []
        while a < n:
            if a % M == 0:
                results.append(a)
            a, b = b, a + b
        return results

fib = Fibonacci()

N = int(input("Enter the term of the fibonacci sequence: "))
M = int(input("Enter the number you want to divide by: "))

FIB = fib.nthterm(N)
div = fib.divisiblebym(N, M)
print(f"The {N}th term is: {FIB}")
print(f"The fibonacci terms that are less than {N}th term and divisible by {M} are: {div}")


# In[ ]:




