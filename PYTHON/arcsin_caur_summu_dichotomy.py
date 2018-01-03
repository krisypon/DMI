import numpy as np
import matplotlib.pyplot as plt

def my_asin(x):
    k = 0
    a = x
    S = a
    #print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
    while k < 500:
        k += 1
        R = ((2*k-1)**2*x*x)/((k*2)*(2*k+1))
        a = a*R
        #a = a * (((2*k-1)**2*x*x)/((k*2)*(2*k+1)))
        S += a
        
    return S

a=-0.99999
b=0.99998
x = np.arange(a,b,0.001)
y = my_asin(x)
plt.plot(x,y)
plt.grid()
#plt.show()

delta_x = 1.e-7 # 0.001
#print delta_x
funa = my_asin(a)
funb = my_asin(b)
if funa * funb > 0:
    print "[%.2f,%.2f] intervala saknu nav"%(a,b)
    print "vai saja intervala ir paru saknu skaits"
    exit()
print "Turpinajums, kad sakne ir"
print "Vertibas intervala galapunktos - ",
print "f(%.2f)=%.2f un f(%.2f)=%.2f"%(a,funa,b,funb)

k=0
while b-a > delta_x:
    k += 1
    x = (a+b)/2
    
    funx = my_asin(x)
    print "%3d. a=%.5f f(%.5f)=%8.5f b=%.5f"%(k,a,x,funx,b)
    if funa * funx > 0:
        a=x
    else:
        b=x
print "Rezultats:"
print "a=%.9f f(%.9f)=%12.9f b=%.9f"%(a,x,funx,b)
print "Aprekins veikts ar %d iteracijam"%(k)
