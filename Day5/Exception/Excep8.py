try:
    a=open("test.txt","r")
    a.write("hey this is python")
finally:
    print "cant not file and write the file"
    a.close()   