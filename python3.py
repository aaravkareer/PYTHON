#Check whether given number is divisible by 3 and 5 both.
a=int(input("enter the number to check:"))
if(a%15==0):
    print("it is divisible by 3 and 5 both")
else:
    print("it is not divisible by 3 and 5 both")


a=int(input("enter the number to check:"))
if(a%5==0):
    print("it is divisible by 5")
else:
    print("it is not divisible by 5")


#Find the greatest among two numbers. If numbers are equal than print “numbers are equal”

a=int(input("enter the number to check:"))    
b=int(input("enter the number to check:"))
if(a>b):
    print("a is greater than b")
elif(a<b):
    print("b is greater than a")
else:
    print("numbers are equal")

#Find the greatest among three numbers assuming no two values are same. 
a=int(input("enter the number to check:"))    
b=int(input("enter the number to check:"))
c=int(input("enter the number to check:"))    
if(a>b):
    if(a>c):
        print("{} is greater than b".format(a))
elif(b>c):
    print("{} is the greatest number".format(b))
else:
    print("{} is the greatest number".format(c))

#Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
a=int(input("enter the coefficient of x^2:"))    
b=int(input("enter the coefficient of x:"))
c=int(input("enter the constant:"))
d=(b**2)-(4*(a*c))
if(d>0 or d==0):
    print("this equation has real roots")
elif(d<0):
    print("this equation has complex roots")
x=(-b+(d**(1/2)))/(2*a)
y=(-b-(d**(1/2)))/(2*a)

print("roots are: {} and {}".format(x,y))




#Find whether a given year is a leap year or not.
a=int(input("enter the year"))
if(a%400==0):
    print("entered year is a leap year")
elif(a%100==0):
    print("entered number is not a leap year")
elif(a%4==0):
    print("entered number is a leap year")
else:
    print("entered number is not a leap year")


#Write a program which takes any date as input and display next date of the calendar
#e.g.
#I/P: day=20 month=9 year=2005 
#O/P: day=21 month=9 year 2005
flag=1
    
d=int(input("Enter the date:"))
m=int(input("Enter the month:"))
y=int(input("Enter the year:"))
if(y%400==0):
    flago=1
elif(y%100==0):
    flago=0
elif(y%4==0):
    flago=1
else:
    flago=0

    
if(m%2!=0 and m<8):
    if(d==31):
        d=1
        m=m+1
    elif(d<31):
        d=d+1
    else:
        print("invalid input")
        flag=0    
elif(m%2==0 and m<8 and m!=2):
    if(d==30):
        d=1
        m=m+1
    elif(d<30):
        d=d+1
    else:
        print("invalid input")
        flag=0    
elif(m%2==0 and m>7 and m<12):
    if(d==31):
        d=1
        m=m+1
    elif(d<31):
        d=d+1
    else:
        print("invalid input")
        flag=0    
elif(m%2!=0 and m>7):
    if(d==30):
        d=1
        m=m+1
    elif(d<30):
        d=d+1
    else:
        print("invalid input")
        flag=0    
        
elif(m==12):
    if(d==31):
        d=1
        m=1
        y=y+1
    elif(d<31):
        d=d+1
    else:
        print("invalid input")
        flag=0    
elif(m==2):
    if(flago==1):
        if(d==29):
            d=1
            m=m+1
        elif(d<29):
            d=d+1
        else:
            print("invalid input")
            flag=0     
    elif(flago==0):
        if(d==28):
            d=1
            m=m+1
        elif(d<28):
            d=d+1
        else:
            print("invalid input")
            flag=0    
            


if(flag==1):
    print("day={} month={} year={}".format(d,m,y))
    
        
        







    











    
    
    
