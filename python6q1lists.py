#lists
sum=0
ns=[[10,20],[30],[40,50,60,70]]
for i in ns:
    for j in i:
        sum=j+sum
    print(sum) 
    sum=0       