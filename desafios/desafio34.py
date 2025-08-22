sal = float(input('Digite seu salario: R$ '))
if sal > 1250:
    au= sal * 0.10
    print('Aumento de 10%: {:.2f}'.format(sal + au))
else:
    au= sal * 0.15
    print('Aumento de 15%: {:.2f}'.format(sal + au))