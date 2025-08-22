import math
an = float(input("Digite o angulo que vc deseja: "))
se = math.sin(math.radians(an))
print('O angulo {} tem o seno de: {:.2f}'.format(an,se))
co = math.cos(math.radians(an))
print('O angulo {} tem o cosseno de: {:.2f}'.format(an,co))
tan = math.tan(math.radians(an))
print('O angulo {} tem o tangente de: {:.2f}'.format(an,tan))