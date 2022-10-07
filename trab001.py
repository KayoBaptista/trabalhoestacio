sexo = str(input("Insira homem ou mulher."))
estatura = float(input('Insira seu altura'))
peso_homem = (altura * 72.7) -58
peso_mulher = (altura * 62.1)-44.7
if genero == 'Homem':
    print('Seu peso ideal é:{}'.format(peso_homem))
else:
    print('Seu peso ideal é:{}'.format(peso_mulher))
"""utilizei if or else e fiz a atribuição de valores(LISTA 1)"""
