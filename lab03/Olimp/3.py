c = 0
for i in range(3):
    s, n = input().split()
    c = c + len(s) * int(n)
print(c)