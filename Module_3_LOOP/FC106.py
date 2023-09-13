# "Write a program to find out the sum of first N terms of the following series 5+55+555+5555+.... up to N terms.
# if N=6 then this series becomes 5+55+555+5555+55555+555555 = 617,280(output)
# if N=3 then this series becomes 5+55+555 =615(output)"  
n=int(input("enter term >> "))
su=0
t=0
for i in range(n):
    term=t*10+5
    su+=term
    t=term
print(su)


