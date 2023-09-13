## Identity matrix 

m1=[[1,0,0],[0,1,0],[0,0,1]]
# m1=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
c=0
for i in m1:
    for j in i:
        c+=1
if c % (c**0.5) == 0:
    I_matrix= True
    for k in range(3):
        for l in range(3):
            if k == l:
                if m1[k][l] != 1:
                    I_matrix=False
                    break
            else:
                if m1[k][l] !=0:
                    I_matrix=False
                    break
    if I_matrix:
            print("Identity matrix")
    else:
        print("Not Identity matrix")
else:
    print("Not Identity matrix")

            






# print(c)
# a=[[1,0,0],[0,1,0],[0,0,1]]
# count=0
# num=0
# i=0
# while i<3:
#     j=0
#     while j<3:
#         if i==j:
#             if a[i][j]==1:
#                 count+=1
#         else:
#             if a[i][j]!=0:
#                 num+=1
#         j+=1
#     i+=1
# if num==0:
#     if  count==3:
#         print('Identity')
# else:
#     print('Not Identity')