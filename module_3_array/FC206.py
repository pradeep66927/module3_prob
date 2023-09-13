## total occurrences of the number 
arr=[1,2,1,5,3,5,3,6,7,5,5,2,8,1,3,5]
n=int(input("enter number >> "))
c=0
for i in arr:
    if i == n:
        c+=1
print(c)
