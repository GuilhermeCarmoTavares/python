num = int(input('Digite um numero para ser convertido: '))
print(''' Escolha uma das bases para conversão:
      [1] Binário 
      [2] Octal
      [3] Hexadecimal
      ''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num)))
elif opcao == 2:
    print('O número {} convertido para octal é {}'.format(num, oct(num)))
else:
    print('O número {} convertido para hexadecimal é {}'.format(num, hex(num)))