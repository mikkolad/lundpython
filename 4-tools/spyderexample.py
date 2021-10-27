#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:03:24 2020

@author: danielmikkola
"""
import numpy as np

@profile
def movmean(xdata, ydata, window):
    ydata_new = np.zeros(len(ydata))
    xdata_new = np.zeros(len(xdata))
    k = int(window/2)
    for i in range(len(ydata)):
        if i < window:
            ydata_new[i] = np.mean(ydata[:(i+k)])
            xdata_new[i] = np.mean(xdata[:(i+k)])
        elif i > len(ydata)-window:
            ydata_new[i] = np.mean(ydata[(i-k):])
            xdata_new[i] = np.mean(xdata[(i-k):])
        else:
            ydata_new[i] = np.mean(ydata[(i-k):(i+k)])
            xdata_new[i] = np.mean(xdata[(i-k):(i+k)])
    return(xdata_new, ydata_new)

x, y = np.loadtxt('xy.txt')
x_med, y_med = movmean(x, y, 100)