s1=set()
s2=set()
n=int(input("enter the no. of  elements in s1 "))
m=int(input("enter the no. of  elements in s1 "))
for i in range(n):
    g=input("enter the fruit")
    s1.add(g)
for i in range(m):
    h=input("enter the fruit")
    s1.add(h)
s3=s1&s2
print(s3)

print(s1-s2)
print(len(s1|s2))