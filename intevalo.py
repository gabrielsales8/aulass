numero_inicial = int(input("Digite o primeiro número inteiro: "))
numero_final = int(input("Digite o segundo número inteiro: "))

if numero_inicial > numero_final:
    numero_inicial, numero_final = numero_final, numero_inicial

print("Números inteiros no intervalo:")
for numero in range(numero_inicial, numero_final + 1):
    print(numero)
