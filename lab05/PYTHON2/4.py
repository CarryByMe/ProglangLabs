s = input().strip()

if '.' in s:
    rub, kop = s.split('.')
else:
    rub, kop = s, '00'

if len(kop) == 0:
    kop = '00'
elif len(kop) == 1:
    kop += '0'

print(f"{rub} rub {int(kop)} kop")