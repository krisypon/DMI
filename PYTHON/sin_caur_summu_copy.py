from math import sin


def mans_sinuss(x):
    k=0
    a=(-1)**0*x**1/(1)
    S = a
    print "Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

    while k < 3:
        k+=1
        a=a*(-1)*x*x/((2*k)*(2*k+1))
        S += a
        print "Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
    
    print "Izdruka no liet.f. Beigas!"
    return S


x = 1. * input("Ievadi argumentu x: ")
y=sin(x)
print "standarta sin(%.2f)=%.2f"%(x,y)
yy = mans_sinuss(x)
print type(yy)
print "mans sin(%.2f)=%.2f"%(x,yy)

x = 1. * input("Ievadi argumentu x: ")
y=sin(x)
print "standarta sin(%.2f)=%.2f"%(x,y)
yy = mans_sinuss(x)
print type(yy)
print "mans sin(%.2f)=%.2f"%(x,yy)


'''
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
