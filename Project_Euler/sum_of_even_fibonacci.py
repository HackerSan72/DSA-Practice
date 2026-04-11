a = 1
b = 2
c = 0
sum = 2
N = int(input())
#print(a)
#print(b)
while a + b <= N:
    c = a + b
    a = b
    b = c
#    print(c)
    if c % 2 == 0:
        sum = sum + c
       # print(c)
print(sum)