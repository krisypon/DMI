import math

x = 1. * input("Ievadi argumentu x: ")

y = math.asin(x)
print "arcsin(%.2f) = %.2f"%(x,y)
print "  "

def my_asin(x):
    k = 0
    a = x
    S = a
    print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
    while k < 10000:
        k += 1
        a = a*((2*k-1)**2*x*x)/(k*2*(2*k+1))
        S += a
        if k == 499:
            print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
        elif k== 500:
            print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
    return S
    
print my_asin(x)
print " "
print "            500"
print "           _____"
print "           \                    2*k+1"
print "            \         (2*k)! * x"
print "asin(%.2f) = >   ______________________"%(x)
print "            /        2             2*k"
print "           /____ (k)! * (2*k+1) * 2"
print "            k=0"

