#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  Planck Spectrum
# The energy spectrum of a black body of temperature T is given by the Planck function

# Bλ (T ) = 2hc2/λ5(1/(exp(hc/λkT ) − 1 ))
#where λ is the wavelength, h is Planck’s constant, k the Boltzmann constant and
#c the speed of light. The differential Bλ (T ) cos θ d dλ is the energy emitted per
#unit surface area and unit time under an angle θ to the surface normal into the solid
#angle d = sin θ dθ dφ (in spherical coordinates) with wavelengths ranging from λ
#to λ + dλ. Integration over all spatial directions and wavelengths yields the Stefan–
#Boltzmann law for the energy flux.

import numpy as np
import scipy.constants as const
import astropy.units as u
import astropy.constants as astconst
import matplotlib.pyplot as plt

def planck_spectrum(wavelength, T):
    """Calculate the Planck spectrum for a given temperature and wavelength."""
    h = const.h
    c = const.c
    k = const.k
    B_T = (2 * h * c**2) / (wavelength**5 * (np.exp(h * c / (wavelength * k * T)) - 1))
    return B_T

def luminosity(R, Teff):
    """Calculate the luminosity using the Stefan-Boltzmann law."""
    sigma = const.sigma  # Stefan-Boltzmann constant
    F = sigma * (Teff**4)  # Radiant flux
    L = 4 * np.pi * (R**2) * F  # Luminosity in watts
    return L

def stellar_parameters(R, Teff):
    """Calculate stellar parameters including lambda_max using Wien's Law."""
    b = 2.897e-3 * u.m * u.K  # Wien's displacement constant
    lambda_max = b / Teff
    return {
        "R": R.to(u.m),
        "Teff": Teff.to(u.K),
        "lambda_max": lambda_max.to(u.m)
    }

# Dictionary of some stars with appropriate parameters
stars = {
    "Barnard's Star": stellar_parameters(0.196 * astconst.R_sun, 3130 * u.K),
    "Sirius A": stellar_parameters(1.711 * astconst.R_sun, 9940 * u.K),
    "Sirius B": stellar_parameters(5800 * u.km, 24800 * u.K),
    "Arcturus": stellar_parameters(25.4 * astconst.R_sun, 4290 * u.K),
    "Betelgeuse": stellar_parameters(6.4e8 * u.km, 3590 * u.K),
}

R_sun = astconst.R_sun.value  # Radius of the Sun in meters
L_sun = astconst.L_sun.value  # Luminosity of the Sun in watts

print("Luminosities and Peak Wavelengths of Stars (relative to solar values):")
for name, params in stars.items():
    params['L'] = luminosity(params['R'].value, params['Teff'].value)
    relative_luminosity = params['L'] / L_sun
    lambda_max = params['lambda_max'].value
    print(f"{name:15s} Luminosity: {params['L']:.1e} W ({relative_luminosity:.1e} L_sun), "
          f"Lambda_max: {lambda_max:.2e} m")

# Initialize array for temperatures
T_sample = np.array([stars[key]['Teff'].value for key in stars] + [5778])  # Add Sun's temperature

# Sort temperatures
T_sample = np.sort(T_sample)

# Define wavelength range
n = 1000
lambda_max = 2e-6  # Maximum wavelength
wavelength = np.linspace(lambda_max / n, lambda_max, n)

def convert_K_to_RGB(T):
    """Convert a Kelvin temperature to an RGB color."""
    T = max(1000, min(T, 40000))
    if T <= 6600:
        red = 255
        green = min(255, 99.4708025861 * np.log(T / 100) - 161.1195681661)
    else:
        red = min(255, 329.698727446 * ((T / 100) - 60) ** -0.1332047592)
        green = min(255, 288.1221695283 * ((T / 100) - 60) ** -0.0755148492)
    blue = 255 if T >= 6600 else (0 if T <= 1900 else min(255, 138.5177312231 * np.log(T / 100 - 10) - 305.0447927307))
    return int(red), int(green), int(blue)

# Plot Planck spectra
plt.figure(figsize=(8, 6), dpi=100)

for T in T_sample:
    color = tuple(val / 255 for val in convert_K_to_RGB(T))  # RGB color corresponding to temperature
    plt.semilogy(1e9 * wavelength, 1e-12 * planck_spectrum(wavelength, T), color=color, label="{:.0f} K".format(T))

plt.xlabel("$\lambda$ [nm]")
plt.xlim(0, 1e9 * lambda_max)
plt.ylabel("$B_\lambda(T)$ [kW m$^{-2}$ nm$^{-1}$ sr$^{-1}$]")
plt.ylim(0.1, 5e4)
plt.legend(loc="upper right", fontsize=8)
plt.title("Planck Spectrum for Various Stellar Temperatures")
plt.savefig("planck_spectrum.png")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




