try:
    a=open("test.txt","w")
    a.write("hey this is python")
except:
    print "cant not file and write the file"
else:
    print "file is succesfully write"
    a.close()   