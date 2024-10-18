from Node2 import Node
class ListaDuplamenteEncadeada:
    def __init__(self) -> None:
        self.head = None
        self.trailer = None
        self.size = 0

    def isEmpty(self): #verifica se a lista está vazia
        return self.head is None

    def __len__(self):
        return self.size

    def addFinal(self, valor):
        valor = str(valor).lower()
        novo = Node(valor)
        pointer = self.head
        while pointer is not None:
            if pointer.data.lower() == valor.lower():
                return 0
            pointer = pointer.next
        if self.head is None:
            self.head = novo
            self.trailer = novo
        else:
            self.trailer.next = novo
            novo.prev = self.trailer
            self.trailer = novo
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

    def inserir(self, valor, index):
        valor = str(valor).lower()
        novo = Node(valor)
        pointer = self.head
        while pointer is not None:
            if pointer.data.lower() == valor.lower():
                return 0
            pointer = pointer.next
        if index == 0:
            if self.head is None:
                self.head = novo
                self.trailer = novo
            else:
                novo.next = self.head
                self.head.prev = novo
                self.head = novo
            self.size += 1
        elif index>= self.size:
            self.addFinal(valor)
        else:
            anterior = self._getnode(index - 1)
            proximo = anterior.next
            novo.next = proximo
            novo.prev = anterior
            if proximo is not None:
                proximo.prev = novo
            anterior.next = novo
            self.size += 1
        return 1

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


    def remover(self, valor): #remove qualquer item da lista, mesmo que esteja no começo ou em outra parte da lista mas não insere no final
        if self.head == None:
            return False
        elif self.head.data.lower() == valor.lower():
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            self.size -= 1
            return True
        else:
            anterior = self.head
            pointer = self.head.next
            while pointer is not None:
                if pointer.data.lower() == valor.lower():
                    anterior.next = pointer.next
                    if pointer.next is not None:
                        pointer.next.prev = anterior
                    self.size -= 1
                    return True
                anterior = pointer
                pointer = pointer.next
        return False

    def ordenaLista(self):
        if self.head is None or self.head.next is None:
            return  # Se a lista estiver vazia ou tiver apenas um elemento, já está ordenada

        trocou = True  # Variável para indicar se houve trocas
        while trocou:
            trocou = False  # No início de cada iteração, assume-se que não haverá trocas
            pointer = self.head  # Começa do primeiro nó

            while pointer.next is not None:  # Percorre a lista até o penúltimo nó
                if pointer.data > pointer.next.data:  # Compara dois nós adjacentes
                    # Se o nó atual for maior que o próximo, troca os valores
                    pointer.data, pointer.next.data = pointer.next.data, pointer.data
                    trocou = True  # Indica que houve uma troca
                pointer = pointer.next  # Avança para o próximo nó

def exibir_menu():
    print("\nEscolha uma opção:")
    print("a) Inserir no início da lista")
    print("b) Verificar se um determinado elemento existe na lista")
    print("c) Excluir um determinado elemento da lista")
    print("d) Mostrar todos os elementos e a quantidade de elementos na lista")
    print("e) Sair do programa")

def main():
    lista = ListaDuplamenteEncadeada()

    while True:
        exibir_menu()
        opcao = input("Digite a sua escolha: ").lower()

        if opcao == 'a':
            valor = input("Digite a informação a ser inserida na lista: ")
            resultado = lista.inserir(valor, 0)
            lista.ordenaLista()
            if resultado != 0:
                print(f"\nInformação '{valor}' inserida na lista.")
            else:
                print("\nInformação já submetida à lista")

        elif opcao == 'b':
            valor = input("Digite a informação a ser verificada: ")
            indice = lista.procuraItem(valor)
            if indice is not False:
                print(f"\nA informação '{valor}' existe na lista, na posição {indice}.")
            else:
                print(f"\nA informação '{valor}' não foi encontrada na lista.")

        elif opcao == 'c':
            valor = input("Digite a informação a ser removida: ")
            resultado = lista.remover(valor)
            if resultado == True:
                print(f"\nInformação '{valor}' removida da lista.")
            else:
                print(f"\nInformação '{valor}' não encontrada na lista.")

        elif opcao == 'd':
            print("Elementos da lista:")
            if lista.isEmpty():
                print("\nNão há nenhum elemento na lista")
            else:
                lista.elementosLista()

        elif opcao == 'e':
            print("Saindo do programa.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()