n = int(input())
r = 0

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        r += a - b

print(r)