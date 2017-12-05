import math

x = 1. * input("Ievadi argumentu x: ")

y = math.asin(x)
print "arcsin(%.2f) = %.2f"%(x,y)
print "  "

def my_asin(x):
    k = 0
    a = x
    S = a

    while k < 500:
        k += 1
        a = a*((2*k-1)**2*2*k*x*x)/(k**2*4*(2*k+1))
        S += a
        if k == 499:
            print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
        elif k== 500:
            print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
    return S

print my_asin(x)



