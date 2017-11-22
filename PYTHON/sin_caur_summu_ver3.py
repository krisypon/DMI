from math import sin
# a0, a1, a2, a3 -> a

x = 1. * input("Ievadi argumentu x: ")

y=sin(x)
print "sin(%.2f)=%.2f"%(x,y)


#a0=(-1)**0*x**1/(1)
a=(-1)**0*x**1/(1)
#S = a0
S = a
print "a = %.2f S = %.2f"%(a,S)

#a1=(-1)**1*x**3/(1*2*3)
#a1=a0*(-1)*x*x/(2*3)
a=a*(-1)*x*x/(2*3)
#S += a1
S += a
print "a = %.2f S = %.2f"%(a,S)

#a2=(-1)**2*x**5/(1*2*3*4*5)
#a2=a1*(-1)*x*x/(4*5)
a=a*(-1)*x*x/(4*5)
#S += a2
S += a
print "a = %.2f S = %.2f"%(a,S)

#a3=(-1)**3*x**7/(1*2*3*4*5*6*7)
#a3=a2*(-1)*x*x/(6*7)
a=a*(-1)*x*x/(6*7)
#S += a3
S += a
print "a = %.2f S = %.2f"%(a,S)

#a4=(-1)**4*x**9/(1*2*3*4*5*6*7*8*9)
#a4=a3*(-1)*x*x/(8*9)
a=a*(-1)*x*x/(8*9)
#S += a4
S += a
print "a = %.2f S = %.2f"%(a,S)

#%.2f - 2 zimes aiz komata

