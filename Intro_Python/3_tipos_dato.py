#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:23:51 2021

@author: bryan
"""
#%%
print("STRINGS - Se usan para textos")

var_str = "Hola!"
var_str2 = "Mundo!"

print(type(var_str))
print(type(var_str2))

#%%

var_str_unido = var_str + " " + var_str2
print(var_str_unido)
#%% 

n = "cadena"
print(n * 10)
#%%

nombre = "Juan"
ciudad = "México"

presentacion = "Hola me llamo {}, soy de {}".format(nombre, ciudad)
print(presentacion)
#%%

import math
pi_str = "los primeros dígitos de pi son: {}".format(math.pi)
print(pi_str)

pi_str = "los primeros dígitos de pi son: {:.2f}".format(math.pi)
print(pi_str)

pi_str = "los primeros dígitos de pi son: {:.0f}".format(math.pi)
print(pi_str)
#%%