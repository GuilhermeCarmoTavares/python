import random
aluno1 = str ( input("Digite nome do primeiro aluno: "))
aluno2 = str ( input("Digite nome do segundo aluno: "))
aluno3 = str ( input("Digite nome do terceiro aluno: "))
aluno4 = str ( input("Digite nome do quarto aluno: "))

lista= (aluno1, aluno2, aluno3, aluno4)
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))