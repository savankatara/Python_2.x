try:
    a=open("myfile.txt","w")
    a.write("hello python")
except:
    print "file going to close"
    a.close()