a=open("new file.txt","w+")
print "please write a file: "
a.write(raw_input("Enter You String : "))
print "file is written"
print "file is close",a.close()
