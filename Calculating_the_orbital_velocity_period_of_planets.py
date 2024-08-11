#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import scipy.constants as const

print(const.G)
print(const.R)
print(const.h)


# In[4]:


import math
import scipy.constants as const
import astropy.constants as astcon

AU = const.au
Yr = const.year

print(" 1 AU =",AU, 'm')
print(" 1 year =",Yr, 'm')

# The distance between Earth and Sun

dse = AU

radius = 10*AU
print("\nradial distance = {:.1f} au".format(radius/AU))

#Calculating the velocity of planets in m/s

def planet_orbitvel():
    import numpy as np
    import math
    import scipy.constants as const
    import astropy.constants as astcon
    
    Name = str(input("Enter the name of the planet :"))
    
    if Name == "Mercury":
         Radius = 57                    
    elif Name == "Venus":
         Radius = 108.2
    elif Name == "Earth":
         Radius = 149.6   
    elif Name == "Mars":
         Radius = 227.9
    elif Name == "Jupiter":
         Radius = 778.6
    elif Name == "Saturn":
         Radius = 1433.5
    elif Name == "Uranus":
         Radius = 2872.5
    elif Name == "Neptune":
         Radius = 4495.1   
    else:
        print("Unknown planet name.")
        return None         
        

    M_sun = 1.989e30 # Mass of the Sun in kg
    seconds_in_days = 86400 # Number of seconds in a day
    G = const.G # Gravitational constant in m^3 kg^-1 s^-2

    Rm = Radius*(1e9)
    T = 2 * math.pi * math.sqrt(Rm**3 / (G * M_sun))
    velocity = (2*(math.pi)*Rm)/T
    return velocity, T

   


# In[5]:


velocity , T = planet_orbitvel()
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))
print(f"The orbital period of is {T:.2f} days.")


# In[7]:


velocity, T = planet_orbitvel()
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))
print(f"The orbital period of is {T:.2f} days.")


# In[8]:


velocity, T = planet_orbitvel()
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))
print(f"The orbital period of is {T:.2f} days.")


# In[9]:


velocity, T = planet_orbitvel()
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))
print(f"The orbital period of is {T:.2f} days.")


# In[10]:


velocity, T = planet_orbitvel()
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))
print(f"The orbital period of is {T:.2f} days.")


# In[11]:


velocity, T = planet_orbitvel()
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))
print(f"The orbital period of is {T:.2f} days.")


# In[12]:


velocity, T = planet_orbitvel()
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))
print(f"The orbital period of is {T:.2f} days.")


# In[13]:


velocity, T = planet_orbitvel()
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))
print(f"The orbital period of is {T:.2f} days.")


# In[ ]:





# In[ ]:




