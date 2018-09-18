a=open("new file.txt","r+")
b=a.read()
print b
position=a.tell()
print position
position=a.seek(0,10)
b=a.read()
print b

print "file is close",a.close()
