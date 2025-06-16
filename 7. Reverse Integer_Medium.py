#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 20:17:30 2025

@author: tom
"""

x = -123

x_str = str(abs(x))

if x < 0:
    limit = 2 ** 31
else:
    limit = 2 ** 31 - 1

if abs(x) > limit:
    out = 0
    
else:
    if x < 0:
        out = -int(x_str[-1::-1])
    else:
        out = int(x_str[-1::-1])
    
if out < 0:
    limit = 2 ** 31
else:
    limit = 2 ** 31 - 1

if abs(out) > limit:
    out = 0

