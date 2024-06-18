from scipy import integrate
from math import *
import numpy as np
import matplotlib as plt
s = input('Enter : ')
f = lambda x:eval(s)
a = (integrate.quad(f,0,5))
print (a[0])

def calculate_definite_integral(expression, lower_bound, upper_bound):
    result = integrate.quad(lambda x: eval(expression), lower_bound, upper_bound)
    print(f"Definite integral from {lower_bound} to {upper_bound} is {result[0]}")