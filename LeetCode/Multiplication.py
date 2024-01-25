from math import ceil

def karatsuba(num1, num2):
    num1str = str(num1)
    num2str = str(num2)

    if num1 < 10 or num2 < 10:
        return num1 * num2

    n = max(len(num1str), len(num2str))
    n2 = n/2

    high1, low1 = int(num1str[:-n2]), int(num1str[-n2:])
    high2, low2 = int(num2str[:-n2]), int(num2str[-n2:])

    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return (z2*10**(n2*2)) + ((z1 - z2 - z0)*10**n2) + z0


a = 5454
b = 4321
print(karatsuba(a, b))
print(a * b)
