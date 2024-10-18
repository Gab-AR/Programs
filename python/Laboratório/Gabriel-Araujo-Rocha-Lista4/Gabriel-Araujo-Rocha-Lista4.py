import os

ARQUIVO = 'pessoas.txt'

def inserir_pessoa():
    cpf = input("Informe o CPF (somente números): ").strip()

    if buscar_por_cpf(cpf, exibir=False):
        print("CPF já cadastrado.")
        return

    nome = input("Informe o nome: ").strip()
    endereco = input("Informe o endereço: ").strip()
    telefones = input("Informe os telefones separados por vírgula: ").split(",")
    
    telefones = [telefone.strip() for telefone in telefones]

    if buscar_por_telefone(telefones, exibir=False):
        print("Um ou mais telefones já estão cadastrados para outra pessoa.")
        return

    with open(ARQUIVO, 'a') as f:
        f.write(f"{cpf};{nome};{endereco};{','.join(telefones)}\n")

    print(f"Pessoa com CPF {cpf} foi cadastrada com sucesso.")

def listar_pessoas():
    if not os.path.exists(ARQUIVO):
        print("Nenhuma pessoa cadastrada.")
        return

    with open(ARQUIVO, 'r') as f:
        pessoas = f.readlines()

    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    
    for pessoa in pessoas:
        cpf, nome, endereco, telefones = pessoa.strip().split(";")
        print(f"CPF: {cpf}\nNome: {nome}\nEndereço: {endereco}\nTelefones: {telefones}\n")

def buscar_por_cpf(cpf=None, exibir=True):
    if cpf is None:
        cpf = input("Informe o CPF para buscar: ").strip()

    if not os.path.exists(ARQUIVO):
        if exibir:
            print("Nenhuma pessoa cadastrada.")
        return None

    with open(ARQUIVO, 'r') as f:
        pessoas = f.readlines()

    for pessoa in pessoas:
        dados = pessoa.strip().split(";")
        if dados[0] == cpf:
            if exibir:
                print(f"CPF: {dados[0]}\nNome: {dados[1]}\nEndereço: {dados[2]}\nTelefones: {dados[3]}")
            return dados

    if exibir:
        print("Pessoa não encontrada.")
    return None

def buscar_por_telefone(telefones=None, exibir=True):
    if telefones is None:
        telefone = input("Informe o telefone para buscar: ").strip()
        telefones = [telefone]

    if not os.path.exists(ARQUIVO):
        if exibir:
            print("Nenhuma pessoa cadastrada.")
        return None

    with open(ARQUIVO, 'r') as f:
        pessoas = f.readlines()

    for pessoa in pessoas:
        dados = pessoa.strip().split(";")
        telefones_pessoa = dados[3].split(',')
        if any(telefone in telefones_pessoa for telefone in telefones):
            if exibir:
                print(f"CPF: {dados[0]}\nNome: {dados[1]}\nEndereço: {dados[2]}\nTelefones: {dados[3]}")
            return dados

    if exibir:
        print("Pessoa não encontrada.")
    return None

def remover_pessoa():
    cpf = input("Informe o CPF da pessoa a ser removida: ").strip()
    
    if not os.path.exists(ARQUIVO):
        print("Nenhuma pessoa cadastrada.")
        return

    with open(ARQUIVO, 'r') as f:
        pessoas = f.readlines()

    with open(ARQUIVO, 'w') as f:
        pessoa_removida = False
        for pessoa in pessoas:
            dados = pessoa.strip().split(";")
            if dados[0] != cpf:
                f.write(pessoa)
            else:
                pessoa_removida = True

    if pessoa_removida:
        print(f"Pessoa com CPF {cpf} foi removida.")
    else:
        print("Pessoa não encontrada.")

def main():
    while True:
        print("\nMenu:")
        print("1. Inserir pessoa")
        print("2. Listar pessoas cadastradas")
        print("3. Buscar pessoa por CPF")
        print("4. Buscar pessoa por Telefone")
        print("5. Remover pessoa por CPF")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            inserir_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            buscar_por_cpf()
        elif opcao == '4':
            buscar_por_telefone()
        elif opcao == '5':
            remover_pessoa()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()