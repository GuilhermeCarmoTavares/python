n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo numero: '))
n3 = int(input('Digite um terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('O maior é: {}'.format(n1))
if n2 > n3:
    print('O maior é: {}'.format(n2))
else:
    print('O maior é: {}'.format(n3))
