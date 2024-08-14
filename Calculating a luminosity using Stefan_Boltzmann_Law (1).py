#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Compute the luminosity of a star using the effective temperature and size by using Stefan- Boltzmann law


# In[6]:


# L = Luminosity of the star # It is obtained by integrating the radiative flux over the whole surface of a star of radius R.
# F = radiative flux # Net energy radiated away per unit surface area and unit time.

import math
import scipy.constants as const

def luminosity_flux():
    
    Name = str(input("Enter the name of a star "))
    Teff = float(input("Enter the effective temperature of star in Kelvin "))
    R = float(input("Enter the radius of star in m "))
    
    sigma = const.sigma
    
    F = sigma * (Teff**4)
    
    L = 4 *(math.pi)*(R**2)*F
    
    print ("The name of a star is", Name)
    return L


# In[10]:


L = luminosity_flux()
print(f"The luminosity of the star is: {L:.2e} watts")


# In[12]:


L = luminosity_flux()
print(f"The luminosity of the star is: {L:.2e} watts")


# In[13]:


L = luminosity_flux()
print(f"The luminosity of the star is: {L:.2e} watts")


# In[ ]:




