
cores = {'azul':'\033[34m',
        'amarelo':'\033[33m',
        'roxo':'\033[35m',
        'ciano':'\033[36m',
        'limpa':'\033[m',
        'vermelho':'\033[31m',
        }



nome= input ('{}Qual o seu nome:{} '.format(cores['azul'],cores['limpa']))

print('{}Vamos calcular numeros {}{}{}{}!'.format(cores['ciano'],cores['limpa'],cores['roxo'],nome,cores['ciano']))

n1 = int(input ('{}Digite um numero: '.format(cores['amarelo'])))
n2 = int(input ('{}Digite outro numero: '.format(cores['azul'])))
s = (n1+n2)

print ('{}A soma dos numeros {}{}{}{}{} e {}{}{}{}{} é {}{}{}{}'.format(cores['vermelho'],cores['limpa'],cores['roxo'],n1,cores['limpa'],cores['vermelho'],cores['limpa'] ,cores['ciano'],cores['vermelho'],cores['limpa'],n2 ,cores['limpa'],cores['amarelo'],s,cores['limpa']))

d = (n1/n2)
m = (n1 * n2)
div = (n1//n2)
pot = (n1 ** n2)

print('{}A divisao é {:.2f} a mult e {} div exata {}, potencia {:.2f}'.format(cores['amarelo'],d, m, div, pot ))




