from random import shuffle

p1 = str(input('Digite o primeiro nome: '))
p2 = str(input('Digite o segundo nome: '))
p3 = str(input('Digite o terceiro nome: '))
p4 = str(input('Digite o quarto nome: '))

lista = [p1,p2,p3,p4]
shuffle(lista)

print("Embaralhados: ")
print(lista)