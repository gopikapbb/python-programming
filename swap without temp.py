a=int(input("Enter the number:"))
b=int(input("Enter the next number:"))
print("BEFORE SWAP")
print("First num is:",a)
print("Second num is:",b)
a=a+b
b=a-b
a=a-b
print("AFTER SWAP")
print("First num is:",a)
print("Second num is:",b)