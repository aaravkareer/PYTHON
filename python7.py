n=int(input("enter the number of elements"))
t=()
for i in range(n):
    a=int(input("enter the element"))
    t+=(a,)
c=t[-1::-1]    
print("the original tuple:",t)
print("the reversed tuple",c)