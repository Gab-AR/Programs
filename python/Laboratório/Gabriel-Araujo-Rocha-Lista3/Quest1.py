def inserir_pessoa(pessoas):
    cpf = input("Informe o CPF (somente números): ").strip()
    
    if cpf in pessoas:
        print("CPF já cadastrado.")
        return

    nome = input("Informe o nome: ").strip()
    endereco = input("Informe o endereço: ").strip()
    telefones = input("Informe os telefones separados por vírgula: ").split(",")
    
    telefones = [telefone.strip() for telefone in telefones]
    
    pessoas[cpf] = (nome, endereco, telefones)
    print(f"\nPessoa com CPF {cpf} foi cadastrada com sucesso.")

def listar_pessoas(pessoas):
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    
    for cpf, dados in pessoas.items():
        nome, endereco, telefones = dados
        print(f"CPF: {cpf}\nNome: {nome}\nEndereço: {endereco}\nTelefones: {', '.join(telefones)}\n")

def buscar_por_cpf(pessoas):
    cpf = input("Informe o CPF para buscar: ").strip()
    
    if cpf in pessoas:
        nome, endereco, telefones = pessoas[cpf]
        print(f"CPF: {cpf}\nNome: {nome}\nEndereço: {endereco}\nTelefones: {', '.join(telefones)}")
    else:
        print("Pessoa não encontrada.")

def buscar_por_telefone(pessoas):
    telefone = input("Informe o telefone para buscar: ").strip()
    
    for cpf, dados in pessoas.items():
        nome, endereco, telefones = dados
        if telefone in telefones:
            print(f"CPF: {cpf}\nNome: {nome}\nEndereço: {endereco}\nTelefones: {', '.join(telefones)}")
            return
    print("Pessoa não encontrada com esse telefone.")

def remover_pessoa(pessoas):
    cpf = input("Informe o CPF da pessoa a ser removida: ").strip()
    
    if cpf in pessoas:
        del pessoas[cpf]
        print(f"Pessoa com CPF {cpf} foi removida.")
    else:
        print("Pessoa não encontrada.")

def main():
    pessoas = {}
    
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
            inserir_pessoa(pessoas)
        elif opcao == '2':
            listar_pessoas(pessoas)
        elif opcao == '3':
            buscar_por_cpf(pessoas)
        elif opcao == '4':
            buscar_por_telefone(pessoas)
        elif opcao == '5':
            remover_pessoa(pessoas)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
