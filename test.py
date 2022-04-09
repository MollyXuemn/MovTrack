# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:03:09 2022

@author: jeremy
"""
import re
import math 
with open("nouveau 6.text") as f:
    vraiecoordonnée=[]
    line=f.readline().rstrip()
    lin1=f.readline().rstrip()[1:]
    g=0
    while line :
        elmtligne=re.split(",", line)
        elmtligne1=re.split(",", line1)
        d=elmtligne[1]
        d=elmtligne[1]
        time=int(d[19]+d[21])
        time1=int(d[19]+d[21])
