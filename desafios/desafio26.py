fr = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} na frase '.format(fr.count('A')))
print('A letra A aparece na primeira posição {} na frase'.format(fr.find('A')+1))
print('A letra A aparece na ultima   posição {} na frase'.format(fr.rfind('A')+1))