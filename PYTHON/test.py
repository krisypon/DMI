import math

x = 1. * input("Ievadi argumentu x: ")
'''
y=math.asin(x)
print "arcsin(%.2f)=%.2f"%(x,y)
S = 0
'''
k=0
a=(math.factorial(2*k)*x**(2*k+1))/(math.factorial(k)**2*(2*k+1)*2**(2*k))
S=a
print "a = %.2f S = %.2f"%(a,S)

k=1
a=a*((2*k-1)**2*2*k*x*x)/(k**2*4*(2*k+1))
S+=a
print "a = %.2f S = %.2f"%(a,S)

k=1
a=a*(2*(2*k-1)*2*k*x*x)/(k**2*4*(2*k+1))
S+=a
print "a = %.2f S = %.2f"%(a,S)


'''
#k=3
a=a*(1*2*3*4*5*6*x*x)/(1*3*7*2**2)
S+=a
print "a = %.2f S = %.2f"%(a,S)

#k=4
a=a*(1*2*3*4*5*6*7*x*x)/(1*3*9*2**2)
S+=a
print "a = %.2f S = %.2f"%(a,S)
'''
'''
#Ar FOR ciklu
S=0

for k in xrange(0, 500, 1):
    l=2*k
    z=2*k+1
    a = (math.factorial(l)*x**(z))/(math.factorial(k)**2*(z)*2**(l))
    S+=a
    if k == 499:
        print "a%d = %.2f S%d = %.2f"%(k,a,k,S)

#Ar WHILE ciklu
'''
'''
k=0
l=2*k
z=l+1
a = (math.factorial(l)*x**(z))/(math.factorial(k)**2*(z)*2**(l))
S=a
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)


while k < 500:
    k+=1
    l=2*k
    z=l+1
    a = (math.factorial(l)*x**(z))/(math.factorial(k)**2*(z)*2**(l))
    S+=a
    if k <20:
        print "a%d = %.2f S%d = %.2f"%(k,a,k,S)
'''
