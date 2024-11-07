import ast
class user:
    def __init__(self,name):
        self.name=name
    def opensavingsaccount (self):
        self.Phone=input("Enter phone no.-> ")
        self.Father=input("Enter father's name-> ")
        self.Aadhar=input("Enter Aadhar no.->")
        self.pan=input("Enter PAN no.")
        self.Alternate=input("Enter alternate phone no.")
        self.Home=input("Enter home address")
        self.Username=input("Enter Username")
        self.Password=input("Set password")
        Phone=self.Phone
        Aadhar=self.Aadhar
        Father=self.Father
        pan=self.pan
        Alternate=self.Alternate
        Home=self.Home
        Username=self.Username
        Password=self.Password
        with open("bank.txt","a")as f:
            f.write("")
        with open("bank.txt") as f:
            line=f.readlines()
            print(line)
                
            for i in line:        
                if i['Aadhar']==Aadhar:
                    print("Aadhar Id already exists")

        while True:    
            ch=int(input("Do you want to buy any of our insurance(Type(1 for yes/0 for no))"))
            if ch==1:
                while(True):
                    a=int(input("Which kind of insurance do you want to buy\n1.Automobile insurance:It covers damages to your vehicle and others in case of an accident\n2.Home insurance: It covers damages to your property and belongings from fire, theft, or natural disasters.\n3.life insurance: It  pays a benefit to your beneficiaries after your death.\n4.health insurance: It covers medical expenses for illnesses or injuries.\n5.disability insurance: It replaces a portion of your income if you become unable to work due to a disability.\n6.long-term care insurance: covers the cost of care for elderly or disabled people who need assistance with daily living activities\n7.umbrella insurance(It covers all type of insurances.)\n8.go back"))
                    if a==8:
                        break
                    if a==1:
                        z=int(input("It starts with:\n1. ₹500/month\n2. ₹1000/month\nPRESS 1 OR 2 TO SELECT or if you don't want to buy press 3"))
                        if z==1:
                            h="₹500/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"Automobile Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==2:
                            h="₹1000/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"Automobile Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==3:
                            break
                    if a==2:    
                        z=int(input("It starts with:\n1. ₹1000/month\n2. ₹2000/month\nPRESS 1 OR 2 TO SELECT or if you don't want to buy press 3"))
                        if z==1:
                            h="₹1000/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"Home Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==2:
                            h="₹2000/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"Home Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==3:
                            break
                    if a==3:    
                        z=int(input("It starts with:\n1. ₹100/month\n2. ₹200/month\nPRESS 1 OR 2 TO SELECT or if you don't want to buy press 3"))
                        if z==1:
                            h="₹100/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"life Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==2:
                            h="₹200/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"life Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==3:
                            break    
                    if a==4:    
                        z=int(input("It starts with:\n1. ₹150/month\n2. ₹300/month\nPRESS 1 OR 2 TO SELECT or if you don't want to buy press 3"))
                        if z==1:
                            h="₹150/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"Health Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==2:
                            h="₹300/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"Health Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==3:
                            break
                    if a==5:    
                        z=int(input("It starts with:\n1. ₹100/month\n2. ₹400/month\nPRESS 1 OR 2 TO SELECT or if you don't want to buy press 3"))
                        if z==1:
                            h="₹100/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"Disiblity Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==2:
                            h="₹400/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','FD':'0','insurance':"Disibility Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==3:
                            break
                    if a==6:    
                        z=int(input("It starts with:\n1. ₹600/month\n2. ₹1000/month\nPRESS 1 OR 2 TO SELECT or if you don't want to buy press 3"))
                        if z==1:
                            h="₹600/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','FD':'0','FD':'0','insurance':"Longterm-care Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==2:
                            h="₹1000/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','FD':'0','FD':'0','insurance':"Longterm-care Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==3:
                            break    
                    if a==7:    
                        z=int(input("It starts with:\n1. ₹3000/month\n2. ₹6000/month\nPRESS 1 OR 2 TO SELECT or if you don't want to buy press 3"))
                        if z==1:
                            h="₹3000/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','FD':'0','insurance':"Umbrella Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==2:
                            h="₹6000/permonth"
                            with open("bank.txt","a") as f:
                                name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','FD':'0','insurance':"Umbrella Insurance->"+h}
                                f.write(str(name)+"\n")
                                break
                        elif z==3:
                            break  
                break        
            elif ch==0:
                with open("bank.txt","a") as f:
                    name={'Aadhar':Aadhar, 'phone':Phone, 'father':Father,'pan':pan,'altPhone':Alternate,'address':Home,'username':Username,'password':Password,'Money':'0','FD':'0','insurance':"No insurance"}
                    f.write(str(name)+"\n") 
                    break
            else:
                print("Enter a valid Input")     
    





    def loan():
            
                q=int(input("we provide these kind of loans:\n1.Education loan\n2.Home loan\n3.Car loan\n4.Business loan\n5.Gold loan\n6.Personal loan\n7.Exit"))
                if q==7:
                    j=0
                    aad=input("Enter your Aadhaar number")
                    qv=int(input("How much money do you want?"))
                    time=int(input("How long(IN YEARS) will your Education take to be completed"))
                    hg=int(input("Do you want loan with collatoral(Press 1) or without collatoral(Press 2)"))
                    while True:
                        if q==1 and hg==1:
                            flag=0
                            l=int(input("In this kind of loan you can pay the money after completing your education(Press1) or you can also pay it monthly while doing your educationPress(2)"))
                            if l==1:
                                print("Interest rate in this kind of loan will be 7%")
                                interest=(((qv*7)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)#I've used Ai in google collab for this problem(to convert a string representing a dictionary into a dictionary)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Education loan(with colatoral and payment after completing->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                            
                            elif l==2:
                                print("Interest rate in this kind of loan will be 6%")
                                interest=(((qv*6)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Education loan(with colatoral and payment while completing->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break
                                    
                                else:
                                    break
                            else:
                                print("Enter a valid number")    

                        elif q==1 and hg==2:
                            flag=0
                            l=int(input("In this kind of loan you can pay the money after completing your education(Press1) or you can also pay it monthly while doing your educationPress(2)"))
                            if l==1:
                                print("Interest rate in this kind of loan will be 11%")
                                interest=(((qv*11)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Education loan(without colatoral and payment after completing->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                            
                            elif l==2:
                                print("Interest rate in this kind of loan will be 10%")
                                interest=(((qv*10)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Education loan(without colatoral and payment while completing->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break
                                                
                                else:
                                    break
                            else:
                                print("Enter a valid number")  
                        elif q==2 and hg==1:   
                            flag=0
                            
                            
                            print("Interest rate in this kind of loan will be 15%")
                            interest=(((qv*15)/100)+qv)/(12*time)
                            sd=str(interest)
                            print("You will have to pay {}/month".format(interest))
                            jh=int(input("do you want to continue(1 for yes/2 for no)"))
                            if jh==1:
                                with open("bank.txt") as f:
                                    line=f.readlines()
                                    print(line)
                                with open("bank.txt","w") as f:
                                    f.write("")
                                
                                    
                                for i in line:
                                    print(i)
                                    zu = ast.literal_eval(i)
                                        
                                    if zu['Aadhar']==aad:
                                        f=open("bank.txt","a")
                                        print("aadhar is matched")
                                        zu['loan']="Home loan(with colatoral->)"+sd+"/month"
                                    
                                        f.write(str(zu)+"\n")
                                        flag=1
                                    else:
                                        with open("bank.txt","a")as f:
                                            f.write(str(zu)+"\n")
                                            flag=1
                                if flag==1:
                                    break            
                            elif jh==2:
                                break
                            else:
                                print("Enter a valid number")
                                            
                            
                        elif q==2 and hg==2:
                            flag=0
                            
                            print("Interest rate in this kind of loan will be 20%")
                            interest=(((qv*20)/100)+qv)/(12*time)
                            sd=str(interest)
                            print("You will have to pay {}/month".format(interest))
                            jh=int(input("do you want to continue(1 for yes/2 for no)"))
                            if jh==1:
                                with open("bank.txt") as f:
                                    line=f.readlines()
                                    print(line)
                                with open("bank.txt","w") as f:
                                    f.write("")
                                
                                    
                                for i in line:
                                    print(i)
                                    zu = ast.literal_eval(i)
                                        
                                    if zu['Aadhar']==aad:
                                        f=open("bank.txt","a")
                                        print("aadhar is matched")
                                        zu['loan']="Home loan(without colatoral->)"+sd+"/month"
                                    
                                        f.write(str(zu)+"\n")
                                        flag=1
                                    else:
                                        with open("bank.txt","a")as f:
                                            f.write(str(zu)+"\n")
                                            flag=1
                                if flag==1:
                                    break            
                                            
                            elif jh==2:
                                break
                            else:
                                print("Enter a valid number")
                                        
                        elif q==3 and hg==1:
                                flag=0
                            
                                print("Interest rate in this kind of loan will be 13%")
                                interest=(((qv*13)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Car loan(with colatoral->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                        
                        elif q==3 and hg==2:
                                flag=0
                                print("Interest rate in this kind of loan will be 15%")
                                interest=(((qv*15)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Car loan(without colatoral->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                            
                                    
                        elif q==4 and hg==1:
                                flag=0
                            
                                print("Interest rate in this kind of loan will be 18%")
                                interest=(((qv*18)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Business loan(with colatoral->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                            
                            
                        elif q==4 and hg==2:
                                flag=0
                            
                                print("Interest rate in this kind of loan will be 20%")
                                interest=(((qv*20)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Business loan(without colatoral->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                            
                            
                        elif q==5 and hg==1:
                                flag=0
                            
                                print("Interest rate in this kind of loan will be 12%")
                                interest=(((qv*12)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Gold loan(with colatoral->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                                                        
                        elif q==5 and hg==2:
                                flag=0
                            
                                print("Interest rate in this kind of loan will be 14%")
                                interest=(((qv*14)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Gold loan(without colatoral->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                            
                            
                        elif q==6 and hg==1:
                                flag=0
                            
                                print("Interest rate in this kind of loan will be 9%")
                                interest=(((qv*9)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Personal loan(with colatoral->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                                            
                            
                        elif q==6 and hg==2:
                                flag=0
                            
                                print("Interest rate in this kind of loan will be 12%")
                                interest=(((qv*12)/100)+qv)/(12*time)
                                sd=str(interest)
                                print("You will have to pay {}/month".format(interest))
                                jh=int(input("do you want to continue(1 for yes/2 for no)"))
                                if jh==1:
                                    with open("bank.txt") as f:
                                        line=f.readlines()
                                        print(line)
                                    with open("bank.txt","w") as f:
                                        f.write("")
                                    
                                        
                                    for i in line:
                                        print(i)
                                        zu = ast.literal_eval(i)
                                            
                                        if zu['Aadhar']==aad:
                                            f=open("bank.txt","a")
                                            print("aadhar is matched")
                                            zu['loan']="Personal loan(without colatoral->)"+sd+"/month"
                                        
                                            f.write(str(zu)+"\n")
                                            flag=1
                                        else:
                                            with open("bank.txt","a")as f:
                                                f.write(str(zu)+"\n")
                                                flag=1
                                    if flag==1:
                                        break            
                                elif jh==2:
                                    break
                                else:
                                    print("Enter a valid number")
                            
                        
                    print("Enter a valid number")       
    def withdrawOrdeposit():
        while True:
            flag=0
            fl=int(input("Press 1. for withdrawal\nPress 2. for deposit"))
            if fl==1:
                aad=input("Enter your Aadhar number")
                mon=input("Enter the money you want to withdraw")
                with open("bank.txt") as f:
                    line=f.readlines()
                    print(line)
                with open("bank.txt","w") as f:
                    f.write("")
                    
                for i in line:
                    print(i)
                    zu = ast.literal_eval(i)
                        
                    if zu['Aadhar']==aad:
                        f=open("bank.txt","a")
                        print("aadhar is matched")
                        monpresent=zu['Money']
                        if int(mon)>int(monpresent):
                            print("Insufficient balance.You need to deposit first")
                            with open("bank.txt","a")as f:
                                f.write(str(zu)+"\n")
                            flag=1

                        else:
                            nx=int(zu['Money'])
                            sd=int(mon)
                            nx=nx-sd
                            zu['Money']=str(nx)
                            f.write(str(zu)+"\n")
                            flag=1
                    else:
                        with open("bank.txt","a")as f:
                            f.write(str(zu)+"\n")
                            flag=1
                if flag==1:
                    break            
            elif fl==2:
                aad=input("Enter your Aadhar number")
                mon=int(input("Enter the money you want to deposit"))
                with open("bank.txt") as f:
                    line=f.readlines()
                    print(line)
                with open("bank.txt","w") as f:
                    f.write("")
                    
                for i in line:
                    print(i)
                    zu = ast.literal_eval(i)
                        
                    if zu['Aadhar']==aad:
                        f=open("bank.txt","a")
                        print("aadhar is matched")
                        monpresent=int(zu['Money'])
                        vc=mon+monpresent
                        zu['Money']=str(vc)
                        f.write(str(zu)+"\n")
                        flag=1
                    
                    else:
                        with open("bank.txt","a")as f:
                            f.write(str(zu)+"\n")
                            flag=1
                if flag==1:
                    break    

    def fixedDeposit():
        while True:
            flag=0
            print("we provide a interest of 12% on our fixed deposit")
            fl=int(input("press 1 to withdraw money from fixed deposit\npress 2 to add money in fixed deposit\n3.exit"))
            if fl==1:
                aad=input("Enter your Aadhar number\n")
                mon=input("Enter the money you want to withdraw\n")
                time=int(input("how much time has it been since you've deposited money"))
                with open("bank.txt") as f:
                    line=f.readlines()
                    print(line)
                with open("bank.txt","w") as f:
                    f.write("")
                    
                for i in line:
                    print(i)
                    zu = ast.literal_eval(i)
                        
                    if zu['Aadhar']==aad:
                        f=open("bank.txt","a")
                        print("aadhar is matched")
                        monpresent=zu['FD']
                        if int(mon)>int(monpresent):
                            print("Insufficient balance")
                            flag=1

                        else:
                            nx=int(zu['FD'])
                            jd=((nx*12)/100)+nx
                            bn=int(mon)
                            ja=jd-bn
                            zu['FD']=str(ja)
                            f.write(str(zu)+"\n")
                            flag=1
                
                                
                    else:
                        with open("bank.txt","a")as f:
                            f.write(str(zu)+"\n")
                            flag=1
                if flag==1:
                    break            
            elif fl==2:
                aad=input("Enter your Aadhar number")
                mon=int(input("Enter the money you want to deposit"))
                with open("bank.txt") as f:
                    line=f.readlines()
                    print(line)
                with open("bank.txt","w") as f:
                    f.write("")
                    
                for i in line:
                    zu = ast.literal_eval(i)
                        
                    if zu['Aadhar']==aad:
                        f=open("bank.txt","a")
                        print("aadhar is matched")
                        monpresent=int(zu['FD'])
                        vc=mon+monpresent
                        zu['FD']=str(vc)
                        f.write(str(zu)+"\n")
                        flag=1
                    
                    else:
                        with open("bank.txt","a")as f:
                            f.write(str(zu)+"\n")
                            flag=1  
                if flag==1:
                    break            
            elif fl==3:
                break
            else:
                print("Enter valid input")
with open("bank.txt","a") as f:
                    name={'Aadhar':"0", 'phone':"0", 'father':"0",'pan':"0",'altPhone':"0",'address':"0",'username':"0",'password':"0",'Money':'0','FD':'0','insurance':"No insurance"}
                    f.write(str(name)+"\n") 
while True:
    e=int(input("Welcome to Aarav's bank\nHow can we help you:\n1.Open a saving's account\n2.Take a loan\n3.Withdraw or Add money\n4.Invest in fixed deposit\n5.exit"))
    aad=input("enter your aadhaar number")
    with open("bank.txt","r") as f:
        line=f.readlines()
        for i in line:
            zu = ast.literal_eval(i)
                
            if zu['Aadhar']==aad:
                flag=0
            else:
                flag=1
                aad1=user(aad)        
    if e==1:
        aad1.opensavingsaccount()
    elif e==2:
        aad1.loan()
    elif e==3:
        aad1.withdrawOrdeposit()
    elif e==4:
        aad1.fixedDeposit()
    elif e==5:
        break
    else:
        print("Enter a valid input")        

    


            
            
      


    
           

                
                
    
    
    
    

    
    
