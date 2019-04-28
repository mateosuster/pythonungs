# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:14:59 2019

@author: Sebastián Pedersen
"""


#para resolver ecuaciones diferenciales
from sympy import *

#para imprimir fórmulas matemáticas
init_printing() 
from IPython.display import display 

# para generar una lista de valores equiespaciados
from numpy import linspace

# para graficara
import matplotlib.pyplot as plt


# defino los nombres de la variable y la función
t = symbols('t') # la variable independiente
y = symbols('y', cls=Function) # la función


# defino la ecuación diferencial
# Eq es la función de Python para definidir ecuaciones diferenciales. La coma es como el igual.
# y(t).diff(t) es la derivada primera
# y(t).diff(t,t) es la derivada segunda
# defino  y'' + 6y' + 9y = 45  (cambiar a gusto)
ecDif = Eq( y(t).diff(t,t) + 6*y(t).diff(t) + 9*y(t), 45 )
#ecDif = Eq( y(t).diff(t) - 3*y(t), 12 ) #ejemplo orden 1:  y' -3y = 12


# defino condiciones iniciales y(0)=1 e y'(0)=2  (cambiar a gusto)
condInic = {y(0): 1, y(t).diff(t).subs(t, 0): 2}
#condInic = {y(0): 4} #ejemplo orden 1:  y(0)=4

# resuelvo la ecuación diferencial
# dsolve es la función de Python para calcular la ec. dif.
# ecDif es la ecuación a calcular
# y(t) son la variable y función a resolver
# ics son las condiciones iniciales
sol = dsolve( ecDif, y(t), ics=condInic )


# imprimo la ecuación diferencial
print 'La ecuación diferencial:'
display(ecDif)
display(condInic)
print "\n" #agrega un renglón en blanco

# imprimo la solución
print 'La solución:'
display(sol)


# si lo anterior forma de mostrar la ec. dif. y la solución no funciona
# se pueden imprimir más rudimentariamente así
# (descomentar este y comentar el anterior)
#print 'La ecuación diferencial:'
#print ecDif
#print condInic
#print "\n" #agrega un renglón en blanco
#print 'La solución:'
#print sol
#print "\n" #agrega un renglón en blanco


#grafico la solución
f = sol.args[1] # me quedo solamente con la fórmula de la solución
lam = lambdify(t, f, modules=['numpy']) #hago la fórmula evaluable
t_vals = linspace(0, 20, 100) #valores de t a usar para evaluar: inicio, fin, paso.
y_vals = lam(t_vals) #evalúo la fórmula en los valores de t


plt.plot(t_vals, y_vals) #hago el gráfico
plt.grid() #que me ponga un grillado en el gráfico
plt.show() #muestro el gráfico




