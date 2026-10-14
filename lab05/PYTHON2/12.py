nums = input().split()

for s in nums:
    x = int(s)
    d = 2
    while x % d != 0:
        d += 1
    print(d, end=' ')