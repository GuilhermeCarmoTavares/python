casa = float(input('Qual o valor da casa? '))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Em quantos anos vc quer pagar? '))

pres = casa / (anos * 12)
minimo = salario * 0.30


print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(pres))

if  pres <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo negado')