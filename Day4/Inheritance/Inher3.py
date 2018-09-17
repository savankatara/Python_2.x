class A:
    def myprint(self):
        print "myprint"
class B(A):
    def display(self):
        print "display"

b=B()
b.display()
b.myprint()