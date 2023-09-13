## minimum element of matrix 
m1=[[9,3,2],
    [4,6,3],
    [7,9,1]]
mn=m1[0][0]
for i in range(3):
    for j in range(3):
        if mn > m1[i][j]:
            mn=m1[i][j]
print(mn)