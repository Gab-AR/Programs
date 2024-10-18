valor = int(input("Digite um valor: "))
numero = 1
resultado = 0
aux = 0
for i in range(valor):
    resultado = numero + aux
    print(f'{numero} ' , end='')
    aux = numero
    numero = resultado
        
