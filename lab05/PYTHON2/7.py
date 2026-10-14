import math

n, t = input().split()
n = int(n)
t = float(t)


print(math.ceil(n * 60 / t))