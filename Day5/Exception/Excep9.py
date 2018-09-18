try:
    
    try:
        a=open("test.txt","r")
        a.write("hey this is python")
    finally:
         
        print "file is closed"
        a.close()
except:
    print "file can not be read"
    
      