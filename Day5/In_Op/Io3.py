try:
    a=open("myfile.txt","r")
    b=a.read()
    print b
except:
    print "file going to close"
    a.close()