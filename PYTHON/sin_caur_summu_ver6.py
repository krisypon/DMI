from math import sin
print "Sin aprekinasana: "
x = 1. * input("Ievadi argumentu x: ")

y=sin(x)
print "sin(%.2f)=%.2f"%(x,y)
print ""

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

    while k < 500:
        k += 1
        R = (-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S += a
        #print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
        if k == 499:
            print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
        elif k == 500:
            print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
    
    #print "Beigas!"
    return "sin(%.2f) caur summu: %.2f"%(x,S)
    
print mans_sinuss(x)
print ""
print "            500"
print "           _____"
print "           \            k   2*k+1"
print "            \       (-1) * x"
print "sin(%.2f) = >   ____________________"%(x)
print "            /"
print "           /____      (2*k+1)!"
print "            k=0"
print ""
print "                                      2"
print "                              (-1) * x"
print "rekurences reizinatajs:  ____________________"
print ""
print "                           k * 2 * (2*k+1)"

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
