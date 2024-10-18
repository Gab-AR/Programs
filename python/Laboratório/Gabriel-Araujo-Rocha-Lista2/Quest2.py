rota = []

def exibir_rota():
    if rota:
        print("Rota atual: ")
        for i, ponto in enumerate(rota):
            print(f"Ponto {i}: {ponto}")
    else:
        print("A rota está vazia.")

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar um novo ponto GPS à rota")
    print("2 - Remover um ponto GPS da rota")
    print("3 - Exibir a rota atual")
    print("4 - Sair do programa")

    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        try:
            x = float(input("Digite a coordenada x: "))
            y = float(input("Digite a coordenada y: "))
            ponto = (x, y)
            rota.append(ponto)
            print(f"Ponto {ponto} adicionado à rota.")
        except ValueError:
            print("Entrada inválida! As coordenadas devem ser números.")
    
    elif escolha == '2':
        if rota:
            try:
                indice = int(input(f"Digite o índice do ponto a ser removido (0 a {len(rota)-1}): "))
                if 0 <= indice < len(rota):
                    ponto_removido = rota[indice]
                    del rota[indice]
                    print(f"Ponto {ponto_removido} removido da rota.")
                else:
                    print("Índice fora dos limites da lista.")
            except ValueError:
                print("Entrada inválida! O índice deve ser um número inteiro.")
        else:
            print("Não há pontos na rota para remover.")

    elif escolha == '3':
        exibir_rota()

    elif escolha == '4':
        print("Encerrando o programa.")
        break

    else:
        print("Escolha inválida! Digite um número entre 1 e 4.")
