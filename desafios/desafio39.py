from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = atual - nasc
tempo = 18 - idade
print('Quem nasceu em {} tem {}'.format(nasc, idade))
if idade > 18:
    print('Deveria ter se alistado há {} anos'.format(tempo))

elif idade == 18:
    print('Deve se alistar IMEDIATAMENTE')
else:
    
    print('Não precisa se alistar ainda faltam {} anos'.format(tempo))