num = int(input('Digite o primeiro número: '))
n2  = int(input('Digite o segundo número: '))
n3  = int(input('Digite o terceiro número: '))

if num > n2 and num > n3:
    print('O maior é {}'.format(num))
elif n2 > n3:
    print('O maior é {}'.format(n2))
else:
    print('iguais')