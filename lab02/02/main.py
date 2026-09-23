a, b, c = input().split()
al = len(a)
bl = len(b)
cl = len(c)

if(al > bl and al > cl):
    print(a)
elif (bl > al and bl > cl):
    print(b)
else:
    print(c)