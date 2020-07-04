def gcd(a, b):
    while(b != 0):
        if(a > b):
            t = a
            a = b
            b = t % b

        else:
            a, b = b, a
            t = a
            a = b
            b = t % b
    return a


print(gcd(60, 96))  # Should be 12
print(gcd(8, 20))  # Should be 4
