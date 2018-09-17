class papa:
    def show(self):
        print "show papa"
class child(papa):
    def show(self):
        print "show child"
c=child()
c.show()