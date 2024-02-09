a={20:'sex',30:"more sex",40:"even more sex"}
#way to input value:
n=int(input("enter the number of elements: "))
d={}
for i in range(n):
    k=int(input("enter key: "))
    v=input("enter value: ")
    if k not in d:
        d[k]=v
    #d.update({k:v})
print(d)

#way to iterate through dict:
#to display keys:
for i in d.items():
    print(i[0])

#to display values and keys:
for i in d.items():
    print(i)

#to display only values:
for i in d.items():
    print(i[1])
