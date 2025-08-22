from random import randint
comp = randint(0,5)
print('='*50)
print('Estou pensando em um numero......')
print('='*50)
usu= int(input('Em que número estou pensando? dica está entre 0 e 5: '))
if usu == comp:
    print('ACERTOU!!!!')
else:
    print('Errou')

print('Numero escolhido: {}'.format(comp))