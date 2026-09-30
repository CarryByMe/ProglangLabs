n, a = map(int, input().split())
c = 0

while c < n:
    if a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0:
        print(a, end=" ")
        c += 1
    a += 1