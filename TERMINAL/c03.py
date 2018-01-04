f = open("meta.bin","rb")
f.seek(0)

ff = open("data.bin","rb")
ff.seek(0)

print "fails meta.bin"
while 1:
	b = f.read(1)
	if not b:
		break
	print hex(ord(b))
print "fails data.bin"
while 1:
	c = ff.read(1)
	if not c:
		break
	print hex(ord(c))
f.close()
