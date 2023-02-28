class student:
        def readstud(self,name,age):
            self.name=name
            self.age=age
        def printstud(self):
            print("Name:",self.name)
            print("Age:",self.age)
s1=student()
s1.readstud("arjun",22)
s1.printstud()