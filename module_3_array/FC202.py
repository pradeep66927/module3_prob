# "Given an array ([10,12,34,11,4,5,1]). Print the last ‘i’ elements of any given array. ‘i’ accepted from the user.
# if i = 3 then your program should print last i elements they are (4,5,1)
# if i = 5 then your program should print last i elements they are (34,11,4,5,1)"
arr = [10,12,34,11,4,5,1]
n=int(input("enter term :"))
n_arr=[None]*n
for i in range(len(arr)-n+1,len(arr)):
    n_arr[len(arr)-n-i]=arr[len(arr)-n+1]
print(n_arr)