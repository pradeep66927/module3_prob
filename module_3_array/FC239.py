## magic square matric 

a=[[4,9,2],[3,5,7],[8,1,6]]  ## this is magic square matrix 
# a=[[2,4,5],                ## this is not magic square matrix 
   #  [5,6,8],
   #  [9,2,4]]
su1=su2=su3=c=0
for i in range(3):
   for j in range(3):
      if i == j:
         su1+=a[i][j]
      else:
         su2+=a[i][j]
         su3+= a[i][j]
if su1 == su2//2:
   c+=1
if su1 == su3//2:
   c+=1
if su2//2 == su3//2:
   c+=1
if c==3:
   print("it's magic square matrix")
else:
   print("it's not a magic squre matrix")



## 2nd way to implement 
# a=[[4,9,2],[3,5,7],[8,1,6]]

# a = [[2, 4, 5],
#      [5, 6, 8],
#      [9, 2, 4]]

# su1 = su2 = su3 = 0

# for i in range(3):
#     for j in range(3): 
#         if i == j:
#             su1 += a[i][j]    ## diagonal 
#         else:
#             su2 += a[i][j]    ## except diagonal rest index
#     su3 += a[i][3-1-i]   ## opposite diagonal

# if su1 == su3:
#     if su2 == 2 *su1 :
#       print("it's magic square matric ")
# else:
#     print("It's not a magic square matrix ")

