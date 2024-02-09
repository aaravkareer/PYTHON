a=int(input("Enter the number of elements="))
s=()
for i in range(a):
    stu=input("enter your name")
    cgpa=float("enter your cgpa")
    s+=((stu,cgpa),)
scgpa=0.0
for i in s:
    scgpa+=cgpa
    print("Student details->\n",i)
print("Average of the class->",scgpa/a)
m=s[0][1]
for i in s:
    if i[1]>m:
        m=i[1]
        k=i[0]
        
