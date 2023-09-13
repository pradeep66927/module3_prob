## maximum , minimum hotday , coolday ,mean
# "In a certain city, the maximum and the minimum temperatures on each day are recorded each month to determine the following at the end of the month: 
# 1. mean maximum temperature in the month 
# 2. mean minimum temperature in the month 
# 3. highest maximum temperature 
# 4. lowest minimum temperature 
# 5. hottest day number of the month 
# 6. coldest day number of the month. 
# Draw a flowchart to show how the desired result can be obtained. Input n from the user where n is number of days."
n=int(input("enter month total day's >> "))
mean_mx=0
mean_mn=0

hot_d=0
cold_d=0
max_arr=[0]*n
min_arr=[0]*n
for i in range (n):
    mx_tody=int(input("today maximum >>  "))
    max_arr[i]=mx_tody
    mn_today = int(input("today min >> "))
    min_arr[i]=mn_today
    mean_mx+=mx_tody
    mean_mn+=mn_today
# print(max_arr)
# print(min_arr)
high_mx=0
low_min=min_arr[0]
for i in range(n):
    if high_mx < max_arr[i]:
        high_mx=max_arr[i]
        hot_d=i+1
    if low_min > min_arr[i]:
        low_min=min_arr[i]
        cold_d=i+1
print("mean maximum temp >>",(mean_mx/n))
print("mean minimum temp >> ",(mean_mn)/2)
print("highest maximum >>",high_mx)
print("lowest minimum >> ",low_min)
print("hottest day is >>",hot_d,"th day ")
print("coldest day is >> ",cold_d,"th day")
    




