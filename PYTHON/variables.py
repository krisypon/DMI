#!/usr/bin/python
# -*- coding: utf-8 -*-

#Noderiga saite
#http://www.cplusplus.com/reference/cstdio/printf/?kw=printf

#https://www.tutorialspoint.com/unix_commands/echo.htm

a=65
print "a kaa dec %d "%(a)
print "a kaa hex %x"%(a)
print "a kaa oct %o"%(a)
print "a kaa simbols %c"%(a)
print "   "
a = 'A'
print type(a)
print "a kaa dec %d "%(ord(a))
print "a kaa hex %x"%(ord(a))
print "a kaa oct %o"%(ord(a))
print "a kaa simbols %c"%(ord(a))
a = '\t'
print type(a)
print "a kaa dec %d "%(ord(a))
print "a kaa hex %x"%(ord(a))
print "a kaa oct %o"%(ord(a))
print "a kaa simbols %c!"%(ord(a))
# ord izmanto kad no simbola jaaiegust skaitlis
a = 8.5
print type(a)
print "a vertiba kaa dec %d "%(a)
print "a vertiba kaa hex %x"%(a)
print "a vertiba kaa oct %o"%(a)
print "a vertiba kaa dailskaitlis ir %10.3f"%(a)
# 10 - pozicijas attelo / 3 - ciparu skaits aiz komata

a = input ("Ievadi a: ")
print "a datu tips ir : %s"%(type(a))

a = raw_input ("Ievadi a: ")
print "a datu tips ir : %s"%(type(a))

a = raw_input ("Vards: ")
b = raw_input ("Uzvards: ")
print "Tevi sauc: %s"%(a + ' ' + b)
print "Tevi sauc: %s"%(a + chr(32) + b)
print "Tevi sauc: %s"%(a + chr(33) + b)
