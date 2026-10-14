s = input()
for c in s[::-1]:
    if c == '(':
        print(')', end='')
    else:
        print('(', end='')
