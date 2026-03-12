import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def g(x):
    return np.exp(-x/4)

def h(x):
    return np.arctan(x)

def f(x):
    return g(x) * h(x)

def dg(x):
    "derivasjon av g(x)"
    return (-1/4)*g(x)

def dh(x):
    "Derivasjon av h(x)"
    return 1/(1+x**2)

def df(x):
    "Produkt av dervasjon g(x)og h(x)"
    return g(x)* dh(x) + h(x)* dg(x)
    

# Vi finner maksmimal punkt når f´(x)= 0
# startverdi til fsolve
x =1
y = f(x)


               
x_max = fsolve(df, x)[0]
y_max = f(x_max)
print(f"Maximal punkt er ({x_max:.4f},{y_max:.4f})")
# Maximal punkt er (1.6907,0.6793)

x= np.linspace(1,2,1000)
y = f(x)
plt.title("Maximal punkt av f(x)")
plt.plot(x,y)
plt.scatter(x_max,y_max)
plt.grid()
plt.savefig("maximum.pdf")
plt.show()





