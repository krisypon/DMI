import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 6.28, 0.01)

y = np.sin(x)
plt.plot(x, y)


def mans_sinuss(x,n):
    k=0
    a=(-1)**0*x**1/(1)
    S = a
    while k < n:
        k+=1
        a=a*(-1)*x*x/((2*k)*(2*k+1))
        S += a   
    return S
yy = mans_sinuss(x,10)
plt.plot(x, yy, 'r')
plt.grid(color='green')

plt.show()
