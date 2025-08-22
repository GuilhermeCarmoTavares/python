
car = int(input('Qual a velocidade do carro? '))
if car >80:
    print('Voce foi multado!')
    multa = (car - 80) * 7
    print('Voce tem que pagar uma multa de R${:.2f}!'.format(multa))
else: 
    print("Voce esta dentro do limite!")

