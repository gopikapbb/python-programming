def pal(n):
    nstr=str(n)
    nrev=nstr[::-1]
    if nstr==nrev:
        return True
    else:
        return False
n=str(input("Enter the number:"))
result=pal(n)
if result:
    print("Palindrom")
else:
    print("Not palindrom")