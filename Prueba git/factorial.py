#*-*-*-*-*Este programa calcula la suma de los factoriales pares*-*-*-*-*-*#

numueroacalcular = int(input("Cual es el numero a calcular? "))
conador1 = 1
contador2 = 0
sumafactorial = 0
factorial = 1
print("")
for contador2 in range(1, numueroacalcular+1):
	if(contador2%2==0):
		for conador1 in range(1, contador2+1):
			factorial=factorial*conador1
	sumafactorial=sumafactorial+factorial
	factorial=1
print("El resultado de la suma de los factoriales pares es: %i" %sumafactorial)
input()
