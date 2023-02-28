a=str(input("Enter a string:"))
x=a.replace(a[0],"$").replace("$",a[0],1)
print(x)