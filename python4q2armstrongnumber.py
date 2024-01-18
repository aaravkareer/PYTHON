#Find whether the given number is Armstrong number
a=int(input("enter the number: "))
count=a
i=a
arm=0

while(a!=0):
    i=a%10
    a=a//10
    arm=arm + i**3
if(count==arm):
    print("It is an armstrong number")
else:
    print("it is not an armstrong number")    
    