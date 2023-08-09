letras = input("Digite uma série de letras separadas por espaço: ")
letras = letras.split()

ascendente = sorted(letras)
descendente = sorted(letras, reverse=True)

print("Letras em ordem alfabética ascendente:", ascendente)
print("Letras em ordem alfabética descendente:", descendente)