from math import hypot

op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
hi = hypot(op,ad)
print('A hipotenusa vai medir: {:.2f}'.format(hi))