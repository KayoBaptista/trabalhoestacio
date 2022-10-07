idades = []
alturas = []
for i in range(1, 6):
    print('%dº Pessoa' %i)
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    idades.append(idade)
    alturas.append(altura)
print('ordem inversa')
print('alturas')
print(alturas[::-1])
print('idades')
print(idades[::-1])
print('ordem lida')
print('alturas')
print(alturas)
print('idades')
print(idades)
""" usei o for e o range e criei uma lista para as alturas e idades"""