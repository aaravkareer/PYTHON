a=int(input("enter the number upto which you want the sum of odd numbers:"))
sum=0
i=0
'''for i in range(1,a):
    if(i%2!=0):
     print("{}+".format(i),end="")
     sum=sum+i
print("={}".format(sum))'''

while(a!=0):
    i=a%10
    a=a//10
    if(i%2!=0):
        print("{}+".format(i),end="")
        sum=sum+i
print("={}".format(sum))


      
  
