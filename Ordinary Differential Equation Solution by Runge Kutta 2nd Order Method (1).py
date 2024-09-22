#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
import matplotlib.pyplot as plt

def rungekuttamethod(f):

    print("Enter the intial value of x")
    x0 = float(input("Enter the value of initial value of x:"))

    print("Enter the final value of x")
    xf = float(input("Enter the value of final value of x:"))

    print("Enter the intial value of y")
    y0 = float(input("Enter the value of initial value of y:"))

    print("Enter the step size h")
    h = float(input("Enter the value of step size h:"))

    n = int ((xf - x0) / h)
    print(" The numbers of steps",n)
    
    x = np.zeros(n+1)
    y = np.zeros(n+1)
  
    x[0] = x0
    y[0] = y0
  
    for i in range(0,n):
        x[i+1] = x[i] + h
        s1 = f(x[i],y[i])
        y[i+1] = y[i] + (h*s1)
        s2 = f(x[i+1],y[i+1])
        y[i+1] = y[i] + (h/2)*(s1 + s2)
    
    
        if y[i+1] > n:
                break
    return x, y       
        
  


# In[3]:


import numpy as np
import math
import matplotlib.pyplot as plt

def f(x,y):
    return 4*(x**2)
  
x, y = rungekuttamethod(f)

plt.scatter(x, y, label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Runge-Kutta Solution')
plt.legend()
plt.show() 
data = [
    f"The values of x: {x}",
    f"The value of y: {y}",
    ]

# Save the data to a text file
with open('Rungekutta2ndorderdata.dat', 'w') as file:
    for line in data:
        file.write(line + '\n')


# In[ ]:




