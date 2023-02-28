a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
c=int(input("Enter num3:"))
if(a>b and a>c):
    print("Num1 is greatest",a)
elif(b>a and b>c):
    print("Num2 is greatest",b)
else:
    print("Num3 is greatest:",c)