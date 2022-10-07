genero = str(input("Insira Homem ou Mulher."))
altura = float(input('Insira seu altura'))
peso_homem = (altura * 72.7) -58
peso_mulher = (altura * 62.1)-44.7
if genero == 'Homem':
    print('Seu peso ideal é:{}'.format(peso_homem))
else:
    print('Seu peso ideal é:{}'.format(peso_mulher))
"""Eu apenas atribui valores nesse progama, e utilizei o if or else para a questão do genero(LISTA 1)"""
