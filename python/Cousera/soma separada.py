n = int(input("Digite o valor de n: "))
soma = 0
while n != 0:
    resto = n%10
    soma = soma + resto
    n = n//10
print(soma)