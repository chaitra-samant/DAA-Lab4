def intMultiplcation(a, b):
    return a * b

def karatsuba(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    
    if a == 0 or b == 0:
        return 0
    if a < 10 or b < 10:
        return a * b

    n = max(len(str(abs(a))), len(str(abs(b))))
    m = n // 2

    pow10m = 10 ** m
    aH, aL = divmod(a, pow10m)
    bH, bL = divmod(b, pow10m)

    z0 = karatsuba(aL, bL)
    z1 = karatsuba(aL + aH, bL + bH)
    z2 = karatsuba(aH, bH)

    return (z2 * 10**(2 * m)) + ((z1 - z2 - z0) * 10**m) + z0

x = 12.35
y = 1234

if not (isinstance(x, int) and isinstance(y, int)):
    raise ValueError("Both inputs must be integers")

res = intMultiplcation(x, y)
print(f"Using Regular Approach: {x} * {y} = {res}")

res = karatsuba(x, y)
print(f"Using Karatsuba's Algorithm: {x} * {y} = {res}")
