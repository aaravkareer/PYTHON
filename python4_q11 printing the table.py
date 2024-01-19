#Print the table for a given number:
a=int(input("enter the number you want to print table of :"))
c=1
for i in range(1,11):
    c=a*i
    print("{}*{}={}".format(a,i,c))