# reverse the array
n=int(input("enter size of array >>"))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("element >>>"))
rev_arr=[0]*n
k=0
for j in range(n-1,-1,-1):
    rev_arr[k]=arr[j]
    k+=1
print(arr)
print(rev_arr)


