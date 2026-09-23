a, b = input().split()
a = int(a)
b = int(b)
while b != 0:

    c = a % b
    a = b
    b = c

print(a)