def multiple():
    N = int(input("No."))
    sum = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    print(sum)
    for i in range(0,N,15):
        sum = sum - i
    #print(sum)
    return sum

multiple()