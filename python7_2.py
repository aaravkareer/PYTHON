n=int(input("enter the number of elements"))
t=()
for i in range(n):
    a=int(input("enter the element"))
    t+=(a,)
t2=()
n2=int(input("enter the number of elements"))
for i in range(n):
    a=int(input("enter the element"))
    t2+=(a,)
t3=()
t3=t+t2    
print(t3)