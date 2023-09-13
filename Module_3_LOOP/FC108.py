###11.  FC108 perfect number till 10,000 ############

n = 10000
for i in range(1, n + 1):
    c = 0
    
    for j in range(1, i):
        if i % j == 0:
            c += j
            
    if c == i:
        print(i, "is a perfect number")
