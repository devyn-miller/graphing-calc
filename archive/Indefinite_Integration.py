import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from numpy import *
from math import *
X = np.arange(-10,10,0.01)
#plot(X,f(X))
s = input('Enter : ')
f = lambda x:eval(s)
def F(x):
    res = np.zeros_like(x)
    for i,val in enumerate(x):
        y,err = integrate.quad(f,0,val)
        res[i]=y
    return res
#plt.plot(X,F(X))
plt.plot(X,F(X),label = s,color = 'black')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
#plt.title(temp.upper())
#plt.style.use('ggplot')
ax = plt.gca()
plt.grid(True)
plt.legend(bbox_to_anchor=(1.1, 1.05))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
plt.close()

def calculate_indefinite_integral(expression):
    def func(x):
        return eval(expression, {"x": x, "__builtins__": None}, np.__dict__)
    
    x_vals = np.linspace(-10, 10, 400)
    y_vals = [integrate.quad(func, 0, x)[0] for x in x_vals]
    
    plt.figure()
    plt.plot(x_vals, y_vals)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Indefinite Integral of the function')
    plt.grid(True)
    plt.show()