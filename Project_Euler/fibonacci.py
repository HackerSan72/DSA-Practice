t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = 1
    b = 2
    c = 0
    sum = 2
#N = int(input())
    while a + b <= n:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            sum = sum + c
    print(sum)