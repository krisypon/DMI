import math

x = 1. * input("Ievadi argumentu x: ")

y=math.asin(x)
print "arcsin(%.2f)=%.2f"%(x,y)

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
