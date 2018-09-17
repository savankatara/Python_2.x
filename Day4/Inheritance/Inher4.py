class A:
    def myprint(self):
        print "myprint"
class B(A):
    def display(self):
        print "display"

class C(B):
    def show(self):
        print "show"

c=C()
c.myprint()
c.display()
c.show()
