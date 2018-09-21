try:
    a=10/0
    print a
except ArithmeticError, a :
    print "this statement is raising an exception",a
else:
    print "welcome"    