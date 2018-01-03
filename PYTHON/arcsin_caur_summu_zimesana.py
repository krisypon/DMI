import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

#y = np.arcsin(x)
#plt.plot(x, y)

def my_asin(x,n):
    k = 0
    a = x
    S = a
    while k < n:
        k += 1
        a = a*((2*k-1)*(2*k-1)*x*x)/(k*2*(2*k+1))
        S += a
    return S

yy = my_asin(x,500)
plt.plot(x, yy, 'r')
plt.show()
