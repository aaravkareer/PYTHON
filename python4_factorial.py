#1. Find a factorial of given number. 

a= int(input("Enter the number you want to calculate factorial of: "))
b=1
for i in range(1,a+1):
    b=i*b
print("factorial of {} is {}".format(a,b)) 
