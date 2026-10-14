n = int(input())
masha = 0
dasha = 0

for i in range(n):
    x = int(input())
    if x % 3 == 0:
        masha += 2
    else:
        dasha += 1

print(f"{masha}:{dasha}")