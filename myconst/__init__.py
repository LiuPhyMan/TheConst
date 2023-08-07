# -*- coding: utf-8 -*-
"""
@author: Liu.Jinbao
@contact: liu.jinbao@outlook.com
@time: 23.May.2023
"""

from scipy.constants import *
eV2J = e
J2eV = 1/eV2J
K2J = k
J2K = 1/K2J
eV2K = eV2J * J2K
K2eV = 1/eV2K
relM2absM = atomic_mass
absM2relM = 1 / relM2absM
e2 = 2.30708e-28 # unit: J m
bohr_radius = physical_constants["Bohr radius"][0]

def nm2Hz(wavelength):
    return 1e9 * c / wavelength