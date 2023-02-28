class rectangle():
    def __init__(self):
        self.len=int(input("Enter the length:"))
        self.bre=int(input("Enter the breadth:"))
    def area(self):
        self.area=(self.len)*(self.bre)
    def perimeter(self):
        self.peri=2*((self.len)+(self.bre))
    def show(self):
        print(self.area)
        print(self.peri)
obj=rectangle()
obj.area()
obj.perimeter()
obj.show()