import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import *
s = str(input("Enter function : "))
temp = s
#s= s.replace('x','(y)')
f = lambda x:eval(s)
# function that returns dy/dt
def model(x,t):
    #k = 0.3
    dxdt = f
    return dxdt

# initial condition
x0 = 5

# time points
t = np.linspace(0,20)

# solve ODE
y = odeint(model,x0,t)
#print (y)

# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

def solve_differential_equation(expression, initial_condition, time_points):
    def model(y, t):
        x = y  # Assuming dy/dt = f(x)
        return eval(expression)
    y = odeint(model, initial_condition, time_points)
    plt.plot(time_points, y)
    plt.show()