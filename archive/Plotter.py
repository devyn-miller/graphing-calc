import matplotlib.pyplot as plt
from math import *
add = 0
s = str(input("Enter function : ")) #Inputs function
temp = s
s= s.replace('x','(x)')
ctr, x, y = -10, [], [] #Setting countert to starting values and x,y to empty lists
while ctr<=10:
        s1 = ''
        add = 0
        s1 = s.replace('x',str(ctr)) #Replaces variable with value at that point
        try:
                add = eval(s1) #Tries to evaluate function at that point, if defined
                y.append(add)
                x.append(ctr)
        except:
                pass#If beyond domain, pass
        ctr+=0.1
#print (x)
#print (y)
plt.figure(num ='GPYTHON')
plt.plot(x,y,label = 'y = '+temp,color = 'black')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
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





import numpy as np
import matplotlib.pyplot as plt

def plot_function(expression):
    x = np.linspace(-10, 10, 400)
    y = eval(expression, {"x": x, "__builtins__": None}, np.__dict__)
    plt.figure()
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Plot of the function')
    plt.grid(True)
    plt.show()