from math import sin
# a0, a1, a2, a3 -> a

x = 1. * input("Ievadi argumentu x: ")

y=sin(x)
print "sin(%.2f)=%.2f"%(x,y)

k=0
a=(-1)**0*x**1/(1)
S = a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

#k=1
k+=1
a=a*(-1)*x*x/((2*k)*(2*k+1))
S += a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

#k=2
k+=1
a=a*(-1)*x*x/((2*k)*(2*k+1))
S += a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

#k=3
k+=1
a=a*(-1)*x*x/((2*k)*(2*k+1))
S += a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
