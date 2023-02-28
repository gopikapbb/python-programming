class area:
	def __init__(self):
		self.area=area
		print("Area of rectangle")
	def length(self):
		length=int(input("Enter the length:"))
		self.length=length
		print("length is:",length)
	def breadth(self):
		breadth=int(input("Enter the braedth:"))
		self.breadth=breadth
		print("breadth is:",breadth)
	def area1(self):
		self.area1=self.length+self.breadth
		print("Area of reactangle is:",self.area1)
a=area()
a.length()
a.breadth()
a.area1()