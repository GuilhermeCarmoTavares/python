nome  = str(input('Digite o seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
separa = nome.split()
print(separa[0],len(separa[0]))

