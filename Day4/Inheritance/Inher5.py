class A:
    def myprint(self):
        print "myprint"
class B():
    def display(self):
        print "display"

class C(B,A):
    def show(self):
        print "show"

c=C()
c.myprint()
c.display()
c.show()
