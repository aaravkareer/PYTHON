n=int(input("enter the number of elements"))
t=()
for i in range(n):
    a=int(input("enter the element"))
    t+=(a,)
positive=0
negative=0
zeroes=0
t2=()
for i in t:
    if(i>0):
        positive+=1
        #t2+=i

    elif(i<0):
        negative+=1
    else:
        zeroes+=1
print("No. of positives={}\nnegatives={}\nzeroes={}".format(positive,negative,zeroes))
#by list comprehension 
t2=([x for x in t if x>0])
print(t2)