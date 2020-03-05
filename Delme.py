# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:07:26 2019

@author: andre
"""
import time
from paraview.simple import *
print("hello")

x = 0
while x < 10:
    vv.hideMeasurementGrid()
    time.sleep(0.500000)
    vv.showMeasurementGrid()
    time.sleep(0.5)
    x+=1
