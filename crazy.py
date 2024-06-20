from dataclasses import dataclass
import matplotlib.pyplot as plt
from math import *
import numpy as np
@dataclass
class Student:
    name:str
    id:str

x=Student("Peter", 1)

def d(f):
    def k(x):
        return f(f(x))
    return k

@d
def f(x):
    if x%2==0:
        return x//2
    return x*3+1



def dif(f):
    a=0.01
    def k(x):
        return (f(x+a)-f(x))/a
    return k

@dif
def dsin(x):
    return np.sin(x)

def plot(func):
    x=np.linspace(-10, 10, 400)
    y=func(x)
    plt.plot(x, y)
    plt.show()

@dif
def dx2(x): return x*x


plot(dx2)
plot(dsin)