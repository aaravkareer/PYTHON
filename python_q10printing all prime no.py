flag=1
for j in range(2,101):
    flag=1
    for i in range (2,j//2):
        if(j%i==0):
            flag=0
    if(flag):
        print(j)        