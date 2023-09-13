# "Given an array ([1,2,3,4,5,6,7]), take a number from the user and check whether it exists in the array or not.
# if number = 7 then output should be ""Yes"" because 7 present in the array.
# if number = 100 then output should be ""No"" because 100 not present in the array."

a=[1,2,3,4,5,6,7]
n=int(input("enter no: "))
flag=0
for i in a:
    if n == i:
        flag+=1
if flag == 1:
    print("YES")
else:
    print("NO")