#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Calculating the period of planets aroung the sun using Kepler's law of planetary motion
# Radius in units million kms
def planet_timeperiod():
    import numpy as np
    import math
    
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
    G = 6.6743e-11 # Gravitational constant in m^3 kg^-1 s^-2

    Rm = Radius*(1e9)
    T = 2 * math.pi * math.sqrt(Rm**3 / (G * M_sun))
    T_days = T/seconds_in_days
    return T_days


# In[3]:


T_days = planet_timeperiod()
print(f"The orbital period of is {T_days:.2f} days.")


# In[4]:


T_days = planet_timeperiod()
print(f"The orbital period of is {T_days:.2f} days.")


# In[5]:


T_days = planet_timeperiod()
print(f"The orbital period of is {T_days:.2f} days.")


# In[6]:


T_days = planet_timeperiod()
print(f"The orbital period of is {T_days:.2f} days.")


# In[7]:


T_days = planet_timeperiod()
print(f"The orbital period of is {T_days:.2f} days.")


# In[8]:


T_days = planet_timeperiod()
print(f"The orbital period of is {T_days:.2f} days.")


# In[9]:


T_days = planet_timeperiod()
print(f"The orbital period of is {T_days:.2f} days.")


# In[10]:


T_days = planet_timeperiod()
print(f"The orbital period of is {T_days:.2f} days.")


# In[ ]:




