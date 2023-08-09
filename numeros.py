numeros = input("Digite uma série de números separados por espaço: ")
numeros = [int(x) for x in numeros.split()]

ascendente = sorted(numeros)
descendente = sorted(numeros, reverse=True)

print("Números em ordem ascendente:", ascendente)
print("Números em ordem descendente:", descendente)