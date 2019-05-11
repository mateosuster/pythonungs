# -*- coding: utf-8 -*-
"""
Created on Sun May 11 15:14:59 2019

@author: Sebastián Pedersen
"""

# Importar los paquetes necesarios
from numpy import linspace
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

# definir la ecuación diferencial o el sistema
def f(t, M):
    #M es una lista
    x=M[0] #la primera posición es la x
    y=M[1] #la segunda posición es la y
    
    # defino el sistema x' = x^2 - y
    #                   y' = 1 - y
    [dxdt, dydt] = [x**2-y, 1-y]
    
    return [dxdt, dydt]


# rango de tiempo donde deseo resolver
# es tiempo inicial, tiempo final, cantidad de pasitos entre inicio y fin
tspan = linspace(0,100,1000) #acá serían 1000 pasos para ir de t=0 a t=100

# condiciones iniciales. Sería [x(0), y(0)]
cond_inic = [-0.9, 1.1]

#resolver la ecuación o sistema
sol = solve_ivp(lambda t, M: f(t, M), [tspan[0],tspan[-1]], cond_inic, t_eval=tspan)


#descomentar y comentar, dependiendo de qué se quiere graficar

#graficar t vs. x(t)
plt.plot(sol.t, sol.y[0], 'k--s')

#graficar t vs. y(t)
#plt.plot(sol.t, sol.y[1], 'k--s')

#graficar x(t) vs. y(t)
#plt.plot(sol.y[0], sol.y[1], 'k--s')

plt.show()