## perfect square between range 
a=int(input('enter lower >> '))
b=int(input('enter upper >>'))
count=0

for i in range(b+1):
    if (i**2)>=a :
        if (i**2)<=b:
            count+=1
            print(i) 
print(count)
