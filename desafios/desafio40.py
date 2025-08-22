from datetime import date
atual  = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
cat = atual - ano

if cat <=9:
    print('Categoria mirim')
elif cat <=14:
     print('Categoria infantil')
elif cat <=19:
     print('Categoria junior')
else:

     print('Categoria senior')
