#2. Count total number of vowels in a given string. 
a=input("enter the string:")
count=0
for i in a:
    if(i in str('aeiou')):
        count=count+1
print("Total number of vowels=",count)