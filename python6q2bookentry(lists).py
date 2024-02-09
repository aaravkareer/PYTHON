num=int(input("enter the number of books: "))
l=[]
print("enter in order:\n1.book name\n2.author name\n3.price of book\n4.published year")
for i in range(0,num+1):
    for j in(0,4):
        print("{}:".format(j+1))
        a=input()
        l.insert(a[i][j])
