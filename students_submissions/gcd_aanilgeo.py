def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
print(gcd(81, 27))  # Expected output: 27
print(gcd(72, 56))  # Expected output: 8
print(gcd(17, 13))  # Expected output: 1
