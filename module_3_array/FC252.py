## subtract the two matrix 
a=[[9,3,4],
   [7,3,8],
   [5,5,7]]
b=[[1,2,1],
   [2,1,3],
   [3,1,4]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(3):
    for j in range(3):
        c[i][j]=a[i][j]-b[i][j]
# print(c)
for k in c:
    print(k)