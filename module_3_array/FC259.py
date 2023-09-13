## sum of diagonal element of matrix 
m1=[[2,3,4],
    [5,6,7],
    [8,9,10]]
su=0
for i in range(3):
    for j in range(3):
        if i == j:
            su+=m1[i][j]
print(su)
