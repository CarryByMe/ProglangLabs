s = input()
ans = 0

for c in s:
    if c.isdigit():
        ans += int(c)

print(ans)  