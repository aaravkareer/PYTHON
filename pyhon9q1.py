#create dictionary of n students where key is rollno and value is cgpad
d={}
n=int(input("enter the number of elements"))
for i in range(n):
    a=int(input("enter the roll number"))
    v=float(input("enter the cgpa"))
    d[a]=v
for i in d.items():
    print(i[0],"->",i[1])
for i in d.items():
    m=i[1]
    k=i[0]
    break;
for i in d.items():
    if i[1]>m:
        m=i[1]
        k=i[0]      
print(k,"is the topper")        
sum=0
for i in d.items():
    sum=sum+i[1]
print("the average cgpa is :",sum/n) 