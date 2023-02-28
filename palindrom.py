n=int(input("Enter the number:"))
temp=n
s=0
r=0
while(n>0):
	s=n%10
	r=r*10+s
	n=n//10
if(r==temp):
	print("Palindrom")
else:
	print("Not a palindrom")