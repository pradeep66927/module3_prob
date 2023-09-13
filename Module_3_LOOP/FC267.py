## given number change into single digit 
n=int(input("enter nu >>"))
su=0
while n>0:
    r=n % 10
    su+=r
    n=n//10
    if n==0 :
        if su >10:
            n=su
            su=0
print(su)