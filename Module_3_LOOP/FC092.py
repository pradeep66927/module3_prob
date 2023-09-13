# Write a program to show how consecutive even numbers starting from 2 are summed up until the sum just exceeds 1000 and then print the sum and the number of even numbers added.
## consecutive number sum
c=2
c_su=0
while c+c_su <1000:
    c_su+=c
    c+=2
print(c_su)