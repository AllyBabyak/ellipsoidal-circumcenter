# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:30:36 2023

@author: a.babyak
"""

from vincenty import vincenty_inverse

print(vincenty_inverse([42.3541165, -71.0693514],[40.7791472, -73.9680804]).m)