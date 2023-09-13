# n=int(input(">>>"))
# for i in range(1,n+1):
#     for j in range(1,i+1,2):
#         print(j,end=" ")
#     print()
n=int(input('>>>'))
i=1
while i <n:
    j=((10**i)//9)**2
    print(j)
    i+=1