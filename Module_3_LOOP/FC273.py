## Euler's totient function 
# n = int(input("Enter a number: "))
# i=1
# count=1
# while i < n:
#     if n % i !=0:
#         count+=1
#     i+=1
# print(count)

# count_coprime = 0
# for j in range(1, n):
#     if gcd(j, n) == 1:
#         count_coprime += 1

# print("Euler's Totient for", n, "is", count_coprime)


# n = int(input("Enter a number: "))
# count = 0

# for num in range(2, n + 1):
#     is_prime = True  # Assume num is prime until proven otherwise
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False  # If num is divisible by any number other than 1 and itself, it's not prime
#             break
    
#     if is_prime:
#         count += 1

# print("The number of prime numbers less than or equal to", n, "is:", count)

# A simple Python3 program
# to calculate Euler's
# Totient Function
 
# Function to return
# gcd of a and b
# def gcd(a, b):
 
#     if (a == 0):
#         return b
#     return gcd(b % a, a)
 
# # A simple method to evaluate
# # Euler Totient Function
# def phi(n):
 
#     result = 1
#     for i in range(2, n):
#         if (gcd(i, n) == 1):
#             result+=1
#     return result

n=int(input('enter num >> '))
i=1
count_m=0
while i < n+1:
    count=0
    j=1
    mn=i
    if i > n:
        mn=n
    while j <= mn:

        if i % j==0 :
            if n % j==0:
                count+=1
        j+=1
    if count == 1:
        count_m+=1
    i+=1
    count=0
print(count_m)



# n = int(input("Enter a number: "))
# count = 0

# for i in range(1, n + 1):
#     common_divisor = 0
#     for j in range(1, min(i, n) + 1):
#         if i % j == 0 and n % j == 0:
#             common_divisor += 1
#     if common_divisor == 1:
#         count += 1

# print("Euler's Totient Function for", n, "is", count)


