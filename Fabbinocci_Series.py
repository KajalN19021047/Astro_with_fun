#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Adding the numbers using the fibonacci series

n = int(input("Enter the number of digits to be added:"))

F_previous = 0
F = 1

for i in range(1,n):
    Ft = F + F_previous
    F_previous = F
    F = Ft
    
    print("The sum of the numbers is ", F)   
    


# In[11]:


# Adding the numbers using the fibonacci series

n = int(input("Enter the number of digits to be added:"))

F_previous = 0
F = 1
n_even = 0
n_odd = 0

for i in range(1,n):
    Ft = F + F_previous
    F_previous = F
    F = Ft
    print("The sum of the numbers is = ", F)
    
    if F%2 == 0:
        n_even +=1
        print(n_even)
    else: 
        n_odd +=1
        print(n_odd)   
    


# In[ ]:




