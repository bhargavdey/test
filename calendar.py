import random
y=random.randint(1,7)
h=random.randint(2001,2024)
print("the year is:",h)
print("day no is: ",y)  


#printing days line
def days():
    print("SUN",end='    ')
    print("MON",end='    ')
    print("TUE",end='    ')
    print("WED",end='    ')
    print("THURS",end='   ')
    print("FRI",end='    ')
    print("SAT",end='    ')
    print('\n')
    

def january():
    #printing january at centre  
    for i in range(1,10,1):
        print(" ",end=' ')
    print("JANUARY")

    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()
        
    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')


    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')


    a=9-y                           #for printing all other dates
    while a<=31:
      
        for a in range(a,a+7,1):
      
            if a>=32:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        
        print('\n')                   #JANUARY
january()
    
    
y=(y+31)%7
if y==0:
    y=7
def february():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("FEBRUARY")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    
    a=9-y                           #for printing all other dates
    if h%4==0:
        f=29
    else:
        f=28
    while a<=f:
        for a in range(a,a+7,1):
            if a>=f+1:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                  #FEBRUARY
february()

y=(y+28)%7
if y==0:
    y=7
if h%4==0:
    y=y+1
def march():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("MARCH")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=31:
        for a in range(a,a+7,1):
            if a>=32:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                     #MARCH
march()


y=(y+31)%7
if y==0:
    y=7
def april():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("APRIL")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=30:
        for a in range(a,a+7,1):
            if a>=31:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                     #APRIL
april()


y=(y+30)%7
if y==0:
    y=7
def may():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("MAY")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=31:
        for a in range(a,a+7,1):
            if a>=32:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                       #MAY
may()


y=(y+31)%7
if y==0:
    y=7
def june():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("JUNE")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=30:
        for a in range(a,a+7,1):
            if a>=31:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                      #JUNE
june()


y=(y+30)%7
if y==0:
    y=7
def july():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("JULY")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=31:
        for a in range(a,a+7,1):
            if a>=32:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                      #JULY
july()


y=(y+31)%7
if y==0:
    y=7
def august():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("AUGUST")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=31:
        for a in range(a,a+7,1):
            if a>=32:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                      #JULY
august()


y=(y+31)%7
if y==0:
    y=7
def september():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("SEPTEMBER")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=30:
        for a in range(a,a+7,1):
            if a>=31:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                 #SEPTEMBER
september()


y=(y+30)%7
if y==0:
    y=7
def october():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("OCTOBER")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=31:
        for a in range(a,a+7,1):
            if a>=32:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                   #OCTOBER
october()


y=(y+31)%7
if y==0:
    y=7
def november():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("NOVEMBER")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=30:
        for a in range(a,a+7,1):
            if a>=31:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                  #NOVEMBER
november()


y=(y+30)%7
if y==0:
    y=7
def december():
    for i in range(1,10,1):
        print(" ",end=' ')
    print("DECEMBER")
        
    #printing a line
    for n in range(1,48,1):
        print("_",end='')
    print('\n')

    days()

    
    for i in range(0,(7*(y-1)+1),1):  #printing initial space according day
        print(" ",end='')

    for j in range(1,9-y,1):
        print(j,end='      ')  #printing dates on first line
    print('\n')

    a=9-y                           #for printing all other dates
    while a<=31:
        for a in range(a,a+7,1):
            if a>=32:
                break
            if a<=9:                    #for giving space for one digit number
                print("",a,end='     ')
      
            else:
                print(a,end='     ')
            a=a+1
        print('\n')                  #DECEMBER
december()