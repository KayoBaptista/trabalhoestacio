peso = int(input("Digite  o peso: "))
excesso = peso - 50
multa = excesso * 4

if peso > 50:
	print("o excesso é de {} e a multa de {}".format(excesso,multa))
else:
	excesso = "0"
	multa = "0"

print ('O excesso de peso foi de {}kg, portanto, a multa é de R${}'.format(excesso,peso))
""" apenas fiz a diferença entre o excesso e a multa que devera ser paga"""