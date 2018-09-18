try:
    a=10/0
    print a
except ArithmeticError :
    print "this statement is raising an exception"
else:
    print "welcome"    