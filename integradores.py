#! /usr/bin/env pyhton

from numpy import *
from pylab import*

print exp(1)

def metodo_euler(f, t0, tf, condini, dt, para):
    y = []
    h = dt
    tiempo = []
    condx = condini
    while t0 < tf:
        #print condx
        y.append(condx)
        tiempo.append(t0)
        #print y
        condx = condx + f(condx,t0,para)*h
        
        t0 = t0 + h
    
    return tiempo, y

def rg4(f, t0, tf, condi, dt, para):
    tiempo = []
    xsalida = []
    h = dt
    t = t0
    x = condi
    while t < tf:
        
        tiempo.append(t)
        xsalida.append(x)
        
        k1 = f(x,t,para)
        k2 = f(x + h*k1*0.5, t + h*0.5, para)
        k3 = f(x + h*k2*0.5, t + h*0.5, para)
        k4 = f(x + h*k3, t + h, para)
        
        x = x + h*(1/6.)*(k1 + 2*k2 + 2*k3 + k4)
        t = t + h
    return tiempo, xsalida

