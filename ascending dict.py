d={}
n=int(input("Enter the number of input:"))
for i in range(n):
    name=input("Enter the name:")
    rollno=input("Enter the roll number:")
    mark=input("Enter the place:")
    d[rollno]={name,mark}
print(sorted(d.values(),reverse=True))