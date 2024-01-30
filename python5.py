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

    
if(m%2!=0 and m<8 and m<=12):
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
elif(m%2!=0 and m>7 and m<=12):
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