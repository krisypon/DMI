#!/usr/bin/python
print "Set s & t:"
s = set ([3,5,9,10])
t = set ("Hello")
print s
print t
print " "
#Adding/removing
s.update([10,37,65])
s.add('e')
t.add('x')
t.update([10, 50, 3])
t.remove ('H')
print "After adding/removing new things"
print s
print t
print " "
print "Operations with sets: "
a = t | s	#Union of t and s
b = t & s	#Intersection of t and s
c = t - s	#Set difference (intem in t, but not in s)
d = t ^ s	#Symmetric difference (intems in t or s, but not both)

print a
print b
print c
print d
