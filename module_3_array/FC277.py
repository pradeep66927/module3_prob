## Remove common character and print rest charactor as string

s1=list(input("enter 1st string >> "))
s2=list(input("enter 2nd string >> "))
uncommon_str=''
c=0
for char1 in s1:
    c+=1
    is_common = False
    for char2 in s2:
        if char1 == char2:
            is_common = True
            break
    if not is_common:
        uncommon_str += char1

for char2 in s2:
    is_common = False
    for char1 in s1:
        if char2 == char1:
            is_common = True
            break
    if not is_common:
        if char2 not in uncommon_str:
            uncommon_str+= char2

print(uncommon_str)





