n, m, c, k = map(int, input().split())

total = n * m
need = total - k

if need <= 0:
    print(0)
else:
    packs = (need + 199) // 200  
    print(packs * c)