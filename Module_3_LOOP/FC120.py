# fibonaci series
n=int(input("enter n >> "))
x=0
y=1
z=0
print(z)
for i in range(n-1):
    x=y
    y=z
    z=x+y
    print(z)


