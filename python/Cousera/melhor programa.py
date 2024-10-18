nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1 + nota2 + nota3)/3
if media >= 7:
    print ("APROVADO")
if media < 4:
    print ("REPROVADO")
if media >=4 and media <7:
    print("EXAME FINAL")
print (media)