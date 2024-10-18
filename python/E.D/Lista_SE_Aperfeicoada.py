from Node import Node
from colorama import Fore, Style, init

init(autoreset=True)

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFinal(self, valor):  # insere um elemento no final da lista
        if self.head is not None:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = Node(valor)
        else:
            self.head = Node(valor)
        self.size += 1

    def _getnode(self, index):  # encontra o nó da lista de acordo com o índice
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")  # return None
        return pointer

    def isEmpty(self):  # verifica se a lista está vazia
        return self.head is None

    def __len__(self):
        return self.size

    def __getitem__(self, index):  # retorna o valor contido no nó desejado
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, valor):  # altera o valor contido no nó desejado
        pointer = self.head
        for i in range(index):
            if pointer is not None:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = valor
        else:
            raise IndexError("list index out of range")

    def procuraItem(self, valor):  # procura por um item na lista através de seu valor
        pointer = self.head
        for i in range(self.size):
            if pointer is not None:
                if pointer.data == valor:
                    return i
                else:
                    pointer = pointer.next
            else:
                raise ValueError("is not in list")
        return False

    def elementosLista(self):  # lista todos os elementos da lista
        pointer = self.head
        for i in range(self.size):
            print(f"{Fore.YELLOW}Elemento {i+1}: {Fore.CYAN}{pointer.data}")
            pointer = pointer.next
        print(f"{Fore.GREEN}Há {Fore.CYAN}{len(self)} {Fore.GREEN}elementos na lista")

    def inserir(self, index, valor):  # insere um elemento em qualquer índice, incluindo o começo e o final
        node = Node(valor)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            anterior = self._getnode(index - 1)  # Obtém o nó anterior à posição de inserção
            if anterior is None or anterior.next is None:  # Caso esteja inserindo no final da lista
                anterior.next = node
            else:
                node.next = anterior.next
                anterior.next = node
        self.size += 1

    def remover(self, valor):  # remove qualquer item da lista
        if self.head == None:
            raise ValueError(f"{valor} is not in list")
        elif self.head.data == valor:
            self.head = self.head.next
            self.size -= 1
        else:
            anterior = self.head
            pointer = self.head.next
            while pointer is not None:
                if pointer.data == valor:
                    anterior.next = pointer.next
                    pointer.next = None
                    self.size -= 1
                    return True
                anterior = pointer
                pointer = pointer.next
        raise ValueError(f"{valor} não está na lista!")

def exibir_menu():
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}Escolha uma opção:")
    print(f"{Fore.YELLOW}a) Inserir no início da lista")
    print(f"{Fore.YELLOW}b) Inserir no final da lista")
    print(f"{Fore.YELLOW}c) Verificar se um determinado elemento existe na lista")
    print(f"{Fore.YELLOW}d) Excluir um determinado elemento da lista")
    print(f"{Fore.YELLOW}e) Mostrar todos os elementos e a quantidade de elementos na lista")
    print(f"{Fore.RED}f) Sair do programa{Style.RESET_ALL}")

def main():
    lista = ListaEncadeadaSimples()

    while True:
        exibir_menu()
        opcao = input(f"{Fore.CYAN}Digite a sua escolha: ").lower()

        if opcao == 'a':
            valor = input(f"{Fore.CYAN}Digite a informação a ser inserida no início: ").lower()
            if lista.procuraItem(valor) is not False:
                print(f"{Fore.RED}Nome '{valor}' já cadastrado.")
            else:
                lista.inserir(0, valor)
                print(f"\n{Fore.GREEN}Informação '{valor}' inserida no início da lista.")

        elif opcao == 'b':
            valor = input(f"{Fore.CYAN}Digite a informação a ser inserida no final: ").lower()
            if lista.procuraItem(valor) is not False:
                print(f"\n{Fore.RED}Nome '{valor}' já cadastrado.")
            else:
                lista.addFinal(valor)
                print(f"\n{Fore.GREEN}Informação '{valor}' inserida no final da lista.")

        elif opcao == 'c':
            valor = input(f"{Fore.CYAN}Digite a informação a ser verificada: ").lower()
            indice = lista.procuraItem(valor)
            if indice is not False:
                print(f"\n{Fore.GREEN}A informação '{valor}' existe na lista, na posição {indice}.")
            else:
                print(f"\n{Fore.RED}A informação '{valor}' não foi encontrada na lista.")

        elif opcao == 'd':
            valor = input(f"{Fore.CYAN}Digite a informação a ser removida: ").lower()
            try:
                lista.remover(valor)
                print(f"\n{Fore.GREEN}Informação '{valor}' removida da lista.")
            except ValueError as e:
                print(f"{Fore.RED}{e}")

        elif opcao == 'e':
            print(f"{Fore.MAGENTA}Elementos da lista:")
            lista.elementosLista()

        elif opcao == 'f':
            print(f"{Fore.RED}Saindo do programa.")
            break

        else:
            print(f"{Fore.RED}Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
