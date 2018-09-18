
a=open("myfile.txt","wr+")
a.write(raw_input("Enter your String data: "))
a.close()
a=open("myfile.txt","wr+")
b=a.read()
print b
print "file going to close"
a.close()