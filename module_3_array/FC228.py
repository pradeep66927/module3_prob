## Decimal number  to roman number convert
d = int(input("Enter decimal digit >> "))

a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
b = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

i = 0
roman_numeral = ''
while d > 0:
    if d >= a[i]:
        d -= a[i]
        roman_numeral += b[i]
    else:
        i += 1
print(roman_numeral)


    




