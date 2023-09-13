# "Write a program to create an array of 7 numbers from the user, and print true if the complete array consists of consecutive numbers or not.
# Consecutive numbers means they should follow the a,a+1,a+2,a+3,a+4...form.
# If user enterd elemets 3,4,5,6,7,8,9 then output should be ""Yes"".
# If user entered elements 9,8,7,6,5,4,3 then output should be ""No"""

n=int(input(" >>"))
a=[None]*n
for i in range(n):
    a[i]=int(input("enter no: "))
c=1
for i in range(n-1):
    j=i+1
    if a[i]+1 == a[j]:
        c+=1
if c==n:
    print("consecutive")
else:
    print("not consecutive")
