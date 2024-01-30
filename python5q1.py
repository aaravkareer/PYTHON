#1. Write a program to count and display the number of capital letters in a given string. 
a=input("enter the string:")
count=0
for i in a:
    if(ord(i)<=90):
        print(i)
    count=count+1    
print("Total number of capital letters:",count)    
