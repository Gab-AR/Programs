import random
numero_aleatorio = random.randint(0, 100)
nome = input("Digite seu nome: ")
print("Ola ",nome, ",tente adivinhar um número inteiro entre 0 e 100.")
palpite = -1
while palpite != numero_aleatorio:
    palpite = int(input("Digite seu palpite: "))
    if numero_aleatorio < palpite:
        print("Tente um numero menor")
    elif numero_aleatorio > palpite:
        print("Tente um numero maior")
print(nome,", você acertou o número mágico: ", numero_aleatorio)

