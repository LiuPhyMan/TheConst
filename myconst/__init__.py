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
Ry_eV = physical_constants["Rydberg constant times hc in eV"][0]
kB = k

nm2m = 1e-9
m2nm = 1 / nm2m
nm2cm = 1e-7
cm2nm = 1/nm2cm
mm2m = 1e-3
m2mm = 1 / mm2m
mm2nm = 1e6
nm2mm = 1 / mm2nm

atm2Pa = 101325.0
Pa2atm = 1/atm2Pa

def nm2Hz_f(wvl_nm):
    return c / (wvl_nm * nm2m)

def Hz2nm_f(nu):
    return (c / nu) * m2nm
