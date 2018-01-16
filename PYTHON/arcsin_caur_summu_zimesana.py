import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

y = np.arcsin(x)
plt.plot(x, y)

def my_asin(x):
    k = 0
    a = x * 1
    S = a
    while k < 500:
        k += 1
        R = (2*k-1)*(2*k-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S += a
    return S

yy = my_asin(x)
plt.plot(x, yy, 'g')
plt.grid(color='green')
plt.show()
