a=str(input("Enter the word:"))
if("ing" in a):
	print(a.replace("ing","ly"))
else:
	print(a+"ing")