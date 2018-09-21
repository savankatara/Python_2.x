try:
    a=open("my.txt","w")
    a.write("hello python")
except:
    print "file going to close"
    a.close()