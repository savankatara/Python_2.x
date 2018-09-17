class A:
    def myprint(self):
        print "myprint"
class B(A):
    def display(self):
        print "display"

class C(A):
    def show(self):
        print "show"

c=C()
b=B()
c.myprint()
b.display()
b.myprint()
c.show()
