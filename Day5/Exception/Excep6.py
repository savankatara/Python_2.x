try:
    a=open("test.txt","r")
    a.write("hey this is python")
except:
    print "cant not file and write the file"
else:
    print "file is succesfully write"
    a.close()   