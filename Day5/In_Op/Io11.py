a=open("new file.txt","wr+")
b=a.write(raw_input("Enter your string : "))

b=a.read()
print b

print "file is close",a.close()
