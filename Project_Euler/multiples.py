def sumN(x, n):
    divisor = (n - 1) // x
    return (divisor * x * (divisor + 1)) // 2

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(sumN(3, n) + sumN(5, n) - sumN(15, n))