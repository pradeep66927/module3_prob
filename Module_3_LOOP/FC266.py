## decimal to binary 
n=int(input("enter decimal no>> "))
bin=' '
while n > 0:
    r=n % 2
    n//=2
    bin=str(r) + bin
print("binary",bin)
