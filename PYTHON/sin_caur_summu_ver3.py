from math import sin
# a0, a1, a2, a3 -> a

x = 1. * input("Ievadi argumentu x: ")

y=sin(x)
print "sin(%.2f)=%.2f"%(x,y)


a0=(-1)**0*x**1/(1)
S = a0
print "a0 = %.2f S = %.2f"%(a0,S)

#a1=(-1)**1*x**3/(1*2*3)
a1=a0*(-1)*x*x/(2*3)
S += a1
print "a1 = %.2f S = %.2f"%(a1,S)

#a2=(-1)**2*x**5/(1*2*3*4*5)
a2=a1*(-1)*x*x/(4*5)
S += a2
print "a2 = %.2f S = %.2f"%(a2,S)

#a3=(-1)**3*x**7/(1*2*3*4*5*6*7)
a3=a2*(-1)*x*x/(6*7)
S += a3
print "a3 = %.2f S = %.2f"%(a3,S)

#a4=(-1)**4*x**9/(1*2*3*4*5*6*7*8*9)
a4=a3*(-1)*x*x/(8*9)
S += a4
print "a4 = %.2f S = %.2f"%(a4,S)

#%.2f - 2 zimes aiz komata

