dis = int(input('Qual será a distancia da viagem? '))
if dis < 201:
    aum = dis * 0.50
    print('A passagem vai sair: R${:.2f}'.format(aum))
else:
    aum = dis * 0.45
    print('A passagem vai sair: R${:.2f}'.format(aum))