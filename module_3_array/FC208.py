## dublicate array remove 
n=int(input("enter how many number want to take in array >> "))
# a=[1,2,3,3,5,3,5,5,6,7]
a=[0]*n
for i  in range(n):
    d=int(input('enter number >>'))
    a[i]=d
i=0
while i < n:
    count=0
    j=i+1
    while j < n:
        if a[j]>0:
            if a[i]>0:
                if a[i]==a[j]:
                    count+=1
        j+=1
    if count>=1:
        print(a[i])   

    i+=1
