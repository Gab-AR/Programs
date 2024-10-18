from Node import Node
class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFinal(self, valor): #insere um elemento no final da lista
        valor = str(valor).lower()
        if self.head is not None:
            pointer = self.head
            while pointer.next is not None:
                if pointer.data.lower() == valor.lower():
                    return 0
                pointer = pointer.next
            if pointer.data.lower() == valor.lower():
                return 0
            pointer.next = Node(valor)
        else:
            self.head = Node(valor)
        self.size += 1
        return 1

    def _getnode(self, index): #encontra o nó da lista de acordo com o índice
            pointer = self.head
            for i in range(index):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError("list index out of range") #return None
            return pointer

    def isEmpty(self): #verifica se a lista está vazia
        return self.head is None
        
    def __len__(self):
        return self.size

    def __getitem__(self, index): #retorna o valor contido no nó desejado
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

    def __setitem__(self, index, valor): #altera o valor contido no nó desejado
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

    def procuraItem(self, valor): #procura por um item na lista através de seu valor
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

    def elementosLista(self): #lista todos os elementos da lista
        pointer = self.head
        for i in range(self.size):
            print(f"Elemento {i+1}: {pointer.data}")
            pointer = pointer.next
        print(f"Há {len(self)} elementos na lista")

    def inserir(self, index, valor): #insere um elemento em qualquer índice, incluindo o começo da lista e o final da lista
        valor = str(valor).lower()
        node = Node(valor)
        pointer = self.head
        while pointer is not None:
            if pointer.data.lower() == valor.lower():
                return 0
            pointer = pointer.next
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
        return 1

    def remover(self, valor): #remove qualquer item da lista, mesmo que esteja no começo ou em outra parte da lista mas não insere no final
        if self.head == None:
            raise ValueError("{} is not in list".format(valor))
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
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(valor))

def exibir_menu():
    print("\nEscolha uma opção:")
    print("a) Inserir no início da lista")
    print("b) Inserir no final da lista")
    print("c) Verificar se um determinado elemento existe na lista")
    print("d) Excluir um determinado elemento da lista")
    print("e) Mostrar todos os elementos e a quantidade de elementos na lista")
    print("f) Sair do programa")

def main():
    lista = ListaEncadeadaSimples()

    while True:
        exibir_menu()
        opcao = input("Digite a sua escolha: ").lower()

        if opcao == 'a':
            valor = input("Digite a informação a ser inserida no início: ").lower()
            if lista.procuraItem(valor) is not False:
                print(f"Nome '{valor}' já cadastrado.")
            else:
                lista.inserir(0, valor)
                print(f"Informação '{valor}' inserida no início da lista.")

        elif opcao == 'b':
            valor = input("Digite a informação a ser inserida no final: ").lower()
            if lista.procuraItem(valor) is not False:
                print(f"Nome '{valor}' já cadastrado.")
            else:
                lista.addFinal(valor)
                print(f"Informação '{valor}' inserida no final da lista.")

        elif opcao == 'c':
            valor = input("Digite a informação a ser verificada: ").lower()
            indice = lista.procuraItem(valor)
            if indice is not False:
                print(f"A informação '{valor}' existe na lista, na posição {indice}.")
            else:
                print(f"A informação '{valor}' não foi encontrada na lista.")

        elif opcao == 'd':
            valor = input("Digite a informação a ser removida: ").lower()
            try:
                lista.remover(valor)
                print(f"Informação '{valor}' removida da lista.")
            except ValueError as e:
                print(e)

        elif opcao == 'e':
            print("Elementos da lista:")
            lista.elementosLista()

        elif opcao == 'f':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()