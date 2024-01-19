a=int(input("enter the element number in fibonacci series"))
sum=0
b=1
c=0
if(a==1):
    print(0)
elif(a==2):
    print(1)    

else:
    for i in range(3,a+1):
        sum=c+b
        c=b
        b=sum
    

    print(sum)