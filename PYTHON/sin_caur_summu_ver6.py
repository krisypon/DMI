from math import sin

x = 1. * input("Ievadi argumentu x: ")

y=sin(x)
print "sin(%.2f)=%.2f"%(x,y)

k=0
a=(-1)**0*x**1/(1)
S = a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

while k < 3:
    k+=1
    a=a*(-1)*x*x/((2*k)*(2*k+1))
    S += a
    print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
    
print "Beigas!"

'''
k+=1
a=a*(-1)*x*x/((2*k)*(2*k+1))
S += a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

k+=1
a=a*(-1)*x*x/((2*k)*(2*k+1))
S += a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
'''
