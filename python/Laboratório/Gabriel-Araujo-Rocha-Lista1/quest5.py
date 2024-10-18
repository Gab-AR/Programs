valor = int(input("Digite um valor: "))
soma = 0
for i in range(valor+1):
    if i%2 == 0:
        soma = soma + i
print(soma)