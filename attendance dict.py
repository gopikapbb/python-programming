a=int(input("Enter the number of inputs:"))
days=int(input("Enter the number of working days:"))
data=[]
for i in range(a):
    name=input("Enter the student name:")
    attendance=int(input("Enter the attendance:"))
    percentage=((attendance/days)*100)
    data.append((name,percentage))
    data.sort(reverse=True)
print("Student data"data)