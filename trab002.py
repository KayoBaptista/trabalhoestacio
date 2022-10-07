horas_ganha = float(input('Digite o quanto você ganhar por horas:'))
horas_trabalhadas = int(input('Digite quantas horas você trabalhou'))
salario_bruto = horas_trabalhadas * horas_ganha
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
Sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - IR - INSS - Sindicato


print('Salario Bruto = R$:{}'.format(salario_bruto))
print('IR = {}'.format(IR))
print('INSS = {}'.format(INSS))
print('Sindicato = {}'.format(Sindicato))
print('Salario liquido = R${}'.format(salario_liquido))

"""Nesse progama eu criei uma variavel pra cada problema e fui atribuindo valores"""