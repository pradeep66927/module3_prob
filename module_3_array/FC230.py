# ## mean mode medium 
n=int(input("enter size of array >>"))
arr=[0]*n
su=0
for i in range(n):
    arr[i]=int(input("element >>>"))
    su+=arr[i]
mean=su//n

dict_count={}
for j in arr:
    if j in dict_count:
        dict_count[j]+=1
    else:
        dict_count[j]=1
# print(dict_count)
m_key=0
m_value=0
for key,value in dict_count.items():
    if value > m_value:
        m_value=value
        m_key=key
# print("mode = ",m_key)
for k in range(n-1):
    for l in range(i):
        if arr[l] > arr[l+1]:
            t=arr[l]
            arr[l]=arr[l+1]
            arr[l+1]=t
print(arr)
if n % 2 == 0:
    for m in range(n//2):
        a=arr[m]
    for p in range((n//2)+1):
        b=arr[p]
    mediu=(a+b)/2
else:
    for s in range((n//2)+1):
        mediu=arr[s]

print("mean = ",mean ,"mediu = ",mediu,"mode= ",m_key)


# array=[1,2,3,3,5,1,6,7,8,9]
# count_dict = {}

# # Count occurrences of each value and populate the dictionary
# for value in array:
#     if value in count_dict:
#         count_dict[value] += 1
#     else:
#         count_dict[value] = 1

# # Print the dictionary containing counts
# print("Value counts:", count_dict)