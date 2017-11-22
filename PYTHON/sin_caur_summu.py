from math import sin

x = 1. * input("Ievadi argumentu x: ")

y=sin(x)
print "sin(%6.2f)=%6.2f"%(x,y)

a=(-1)**0*x**1/(1)
S = a
print "a = %6.2f S = %6.2f"%(a,S)

for i in xrange(2, 20, 2):
    a=a*(-1)*x*x/(i*(i+1))
    S += a
    print "a = %6.2f S = %6.2f"%(a,S)

