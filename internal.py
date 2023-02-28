def isPalindrome(i):
    t=i
    r=0
    s=0
    while(i>0):
        s=i%10
        r=r*10+s
        i=i//10
    p.append(i)
    print("palindrome is",p)
def isPrme(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
            else:
                prim.append(num)
    print(prim)
def isPerfect(n):
    sum=0
    for i in range(1, n):
        if n % i == 0:
            sum=sum+i
    if sum == n:
        per.append(sum)
    print("perfect is ",per)
 
l=[121,153,6,13531,7,2,28]
p=[]
prim=[]
per=[]
for i in l:
    isPalindrome(i)
    isPrme(i)
    isPerfect(i)