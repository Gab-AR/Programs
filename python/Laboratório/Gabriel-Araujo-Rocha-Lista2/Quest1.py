alunos = []
opcao = 0

def pesquisar(nome):
    if nome in alunos:
        return False
    else:
        return True
    
while True:
    while opcao <1 or opcao >5:
        print("")
        print("Digitar '1' para inserir um novo aluno na lista.\nDigitar '2' para buscar um aluno na lista.\nDigitar '3' para exibir a lista de alunos em ordem alfabética.\nDigitar '4' para remover um aluno da lista.\nDigitar '5' para sair do programa.")
        print("")
        opcao = int(input("ESCOLHA UMA OPÇÃO ACIMA:\n"))

    if opcao == 1:
        print("")
        print("INSERIR NOVO ALUNO NA LISTA")
        print("")
        nome = input("Digite o nome do aluno\n")
        if pesquisar(nome):
            alunos.append(nome)
            alunos.sort()
        else:
            print("Aluno já cadastrado!")
    elif opcao == 2:
        print("")
        print("PESQUISAR ALUNO NA LISTA")
        print("")
        nome = input("Digite o nome do aluno\n")
        if not pesquisar(nome):
            print("Aluno encontrado na lista.")
        else:
            print("Aluno não cadastrado!")
    elif opcao == 3:
        print("")
        print("LISTA DE ALUNOS EM ORDEM ALFABÉTCA")
        print("")
        print(alunos)
    elif opcao == 4:
        print("")
        print("REMOVER NOVO ALUNO DA LISTA")
        print("")
        nome = input("Digite o nome do aluno\n")
        if not pesquisar(nome):
            alunos.remove(nome)
            alunos.sort()
        else:
            print("Aluno não encontrado na lista!")
    elif opcao == 5:
        break

    opcao = 10