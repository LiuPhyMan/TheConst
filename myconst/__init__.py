# -*- coding: utf-8 -*-
"""
@author: Liu.Jinbao
@contact: liu.jinbao@outlook.com
@time: 23.May.2023
"""
from math import pi as _pi
from scipy.constants import *
eV2J = e
J2eV = 1/eV2J
K2J = k
Hz2J = h
J2Hz = 1/Hz2J
K2Hz = K2J * J2Hz
Hz2K = 1 / K2Hz
eV2Hz = eV2J * J2Hz
Hz2eV = 1 / eV2Hz
J2K = 1/K2J
eV2K = eV2J * J2K
K2eV = 1/eV2K
relM2absM = atomic_mass
absM2relM = 1 / relM2absM
e2 = 2.30708e-28 # unit: J m
bohr_radius = physical_constants["Bohr radius"][0]
light_c = c
Ry_J = physical_constants["Rydberg constant times hc in J"][0]

def nm2Hz_f(wvl_nm):
    return 1e9 * c / wvl_nm

def Hz2nm_f(nu):
    return 1e9 * c / nu
