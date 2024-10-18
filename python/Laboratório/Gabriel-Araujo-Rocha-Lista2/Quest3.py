conjunto1 = set()
conjunto2 = set()
conjunto3 = set()

conjunto1.update(["vermelho", "azul", "verde"])
conjunto2.update(["azul", "amarelo", "preto"])
conjunto3.update(["verde", "amarelo", "branco"])

def escolher_conjuntos():
    while True:
        try:
            conj1 = int(input("Selecione o primeiro conjunto (1, 2 ou 3): "))
            conj2 = int(input("Selecione o segundo conjunto (1, 2 ou 3): "))
            if conj1 in [1, 2, 3] and conj2 in [1, 2, 3]:
                if conj1 == 1:
                    conjunto_a = conjunto1
                elif conj1 == 2:
                    conjunto_a = conjunto2
                else:
                    conjunto_a = conjunto3
                
                if conj2 == 1:
                    conjunto_b = conjunto1
                elif conj2 == 2:
                    conjunto_b = conjunto2
                else:
                    conjunto_b = conjunto3
                
                return conjunto_a, conjunto_b
            else:
                print("Seleção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira números inteiros.")

while True:
    print("\nEscolha uma opção:")
    print("1 - União entre dois conjuntos de cores")
    print("2 - Interseção entre dois conjuntos de cores")
    print("3 - Diferença entre dois conjuntos de cores")
    print("4 - Sair do programa")

    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        conjunto_a, conjunto_b = escolher_conjuntos()
        resultado = conjunto_a.union(conjunto_b)
        print(f"União dos conjuntos: {resultado}")
    
    elif escolha == '2':
        conjunto_a, conjunto_b = escolher_conjuntos()
        resultado = conjunto_a.intersection(conjunto_b)
        print(f"Interseção dos conjuntos: {resultado}")
    
    elif escolha == '3':
        conjunto_a, conjunto_b = escolher_conjuntos()
        resultado = conjunto_a.difference(conjunto_b)
        print(f"Diferença entre os conjuntos: {resultado}")
    
    elif escolha == '4':
        print("Encerrando o programa.")
        break
    
    else:
        print("Escolha inválida! Digite um número entre 1 e 4.")
