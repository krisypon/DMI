import sys
m = open("meta.bin","rb" )
m.seek(0)

d = open("data.bin","rb")

k=0

while 1:
	a = m.read(1)
	if not a:
		break

	k+=ord(a)
	d.seek(k)
	b = d.read(1)
	if not b:
		break
	
	c = m.read(1)
			
	xor = ord(b) ^ ord(c)
#	printf chr(xor),
	sys.stdout.write(chr(xor))

m.close()
d.close()
print ("")
