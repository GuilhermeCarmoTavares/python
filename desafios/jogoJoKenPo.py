from random import randint
from time import sleep
import emoji

emoj=[emoji.emojize(':victory_hand:'), emoji.emojize(':raised_hand:'), emoji.emojize(':raised_fist:')]

cores = {'azul':'\033[34m',
        'ciano':'\033[36m',
        'limpa':'\033[m',
        'vermelho':'\033[31m',
        'roxo':'\033[35m',
        'amarelo':'\033[33m',
        }

print('----- PEDRA, PAPEL, TESOURA -----')
print('''{}Esolha uma opção:
    [0]PEDRA {}
    [1]PAPEL {}
    [2]TESOURA {} '''.format(cores['roxo'],emoji.emojize(':raised_fist:'), emoji.emojize(':raised_hand:'),emoji.emojize(':victory_hand:')))


escolha = int(input('Sua opção:{} '.format(cores['limpa'])))
itens= ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0,2)


print('{}'.format(cores['ciano']))
print('>=<'*50) 
print('{}'.format(cores['limpa']))


print('{}JO!'.format(cores['roxo']))
sleep(1)
print('{}KEN!!'.format(cores['amarelo']))
sleep(1)
print('{}PO!!!'.format(cores['roxo']))
sleep(1)

if comp == escolha:
    print('')
    print('''{}EMPATE!!!!{}
Maquina escolheu: {} 
Jogador escolheu: {}'''.format(cores['azul'],cores['limpa'],itens[comp],itens[escolha]))


elif (comp == 0 and escolha == 1) or (comp == 1 and escolha == 2 ) or (comp == 2 and escolha == 0):
    print('')
    print('''{}GANHOU!!!!{} 
Maquina escolheu: {}  
Jogador escolheu: {}'''.format(cores['ciano'],cores['limpa'],itens[comp],itens[escolha]))
   

else:
    print('')
    print('''{}PERDEU!!!!{}
Maquina escolheu: {} 
Jogador escolheu: {}'''.format(cores['vermelho'],cores['limpa'],itens[comp],itens[escolha]))
    

print('{}'.format(cores['ciano']))
print('>=<'*50)