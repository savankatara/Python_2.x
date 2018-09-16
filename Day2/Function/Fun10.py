def printme(a,*b):
    "This prints a passed string into this function"
    print a
    for c in b:
        print c
   

# Now you can call printme function
printme(50)
printme(1,20,30,40)
