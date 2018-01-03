import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1.0, 1.0, 0.01)

y = np.arcsin(x)
plt.plot(x, y)

def my_asin(x,n):
    k = 0
    a = x
    S = a
    while k < 500:
        k += 1
        a = a*((2*k-1)**2*2*k*x*x)/(k**2*4*(2*k+1))
        S += a
    return S

yy = my_asin(x,10)
plt.plot(x, yy+0.5, 'r')
plt.show()
