#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Regression modal
#Linear regression function

def regression1(x,y):
    
    import numpy as np
    import math
    import matplotlib.pyplot as plt

    
    print("the number of data points are")
    n = float(input("Enter the value of n:"))

    x_mean = np.mean(x)
    y_mean = np.mean(y)
    xy_mean = np.mean(x*y)
    xx_mean = np.mean(x*x)

    b = (n*xy_mean - x_mean*y_mean)/ (n*xx_mean - x_mean*x_mean)

    a = (y_mean - b*x_mean)/n
    
    ycal  = a + b*x
    sumx_meany_mean = np.sum((x - x_mean)*(y - y_mean))
    sumx_mean2 = np.sum((x-x_mean)**2)
    sumy_mean2 = np.sum((y-y_mean)**2)

    
    r = sumx_meany_mean/math.sqrt(sumx_mean2*sumy_mean2)

    print("The slope of the of line is", a)
    print("The value of the intercept", b)
    print("The value of the coefficient of regression", r)

    if r==0:
        print("Not correlated")
    elif r<0 and -1<r<-0.5:
         print("Strong negative correlation")
    elif r<0 and r>-0.5 :
         print("Weak negative correlation")
    elif r>0 and 0.5<r<1:
         print("Strong positive correlation")
    elif r>0 and r< 0.5 : 
         print("Weak positive correlation")



    return a,b,r,ycal


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

temp_data= np.loadtxt('dl8-null.dat')
x= temp_data[0:,6]
y= temp_data[0:,0]

a,b,r,ycal = regression1(x,y)

plt.scatter(x, y, color ='blue', label='data points')
plt.plot(x, ycal, color ='red', label= 'fitted-line')
plt.title('Δ8-log(τ)')
plt.xlabel('log(τ)')
plt.ylabel('Δ8')
plt.show()
np.savetxt('DEL8-AGE.dat', (a,b,r))


# In[ ]:




