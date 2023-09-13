## m=lower , n=upper including both between all number multiplication 
m=int(input("lower nu >> "))
n=int(input("upper nu >> "))
mul=1
for i in range(m ,n+1):
    mul*=i
print(mul)