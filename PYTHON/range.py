#!/usr/bin/python

a = range(5)
print "a = range(5)"		#a = [0,1,2,3,4]
print (a)
print " "

b = range(1, 8)
print "b = range(1, 8)"		#b = [1,2,3,4,5,6,7]
print (b)
print " "

c = range(0, 14, 3)
print "c = range(0, 14, 3)"	#c = [0,3,6,9,12]
print (c)
print " "

d = range(8, 1, -1)
print "d = range(8, 1, -1)"	#d = [8,7,6,5,4,3,2]
print (d)
print " "

for i in xrange(1,10):
	print "2 to the %d power is %d" % (i, 2**i)
print" "

h = range (100)
y = range (0, 100, 5)
print h
print y
