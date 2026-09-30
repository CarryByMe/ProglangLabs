a, b, c = map(int, input().split())

if a < b:
    left = a
    right = b
else:
    left = b
    right = a

if c < left:
    print(left - c)
elif c > right:
    print(c - right)
else:
    print(0)