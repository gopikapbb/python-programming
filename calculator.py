a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
ch=input("Enter the choice [+,-,%,*,/]:")
if ch=='+':
	print("SUM:",a+b)
elif ch=='-':
	print("SUB:",a-b)
elif ch=='*':
	print("MUL:",a*b)
elif ch=='/':
	print("Div:",a/b)
else:
	print("REM:",a%b)