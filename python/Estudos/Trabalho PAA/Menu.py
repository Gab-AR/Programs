from BubbleSort import *
from MergeSort import *
import time

def menu_tamanho():
    while True:
        print("\n")
        print("Escolha o tamanho da lista:")
        print("1. 100")
        print("2. 1000")
        print("3. 5000")
        print("4. 30000")
        print("5. 50000")
        print("6. 100000")
        print("7. 150000")
        print("8. 200000")
        print("0. Voltar")
        tamanho_escolha = input("Escolha uma opção: ")
        if tamanho_escolha == '0':
            return 0
        elif tamanho_escolha in [str(i) for i in range(1, 9)]:
            return int(tamanho_escolha)      
        else:
            print("Opção inválida, tente novamente.")

def menu_ordem():
    while True:
        print("\n")
        print("Escolha a ordem dos números no arquivo:")
        print("1. Crescente")
        print("2. Decrescente")
        print("3. Aleatória")
        print("0. Voltar")
        ordem_escolha = input("Escolha uma opção: ")
        if ordem_escolha == '0':
            break
        elif ordem_escolha == '1':
            tamanho = menu_tamanho()
            match tamanho:
                case 0:
                    break
                case 1:
                    caminho = "ascending_numbers_100.txt"
                case 2:
                    caminho = "ascending_numbers_1000.txt"
                case 3:
                    caminho = "ascending_numbers_5000.txt"
                case 4:
                    caminho = "ascending_numbers_30000.txt"
                case 5:
                    caminho = "ascending_numbers_50000.txt"
                case 6:
                    caminho = "ascending_numbers_100000.txt"
                case 7:
                    caminho = "ascending_numbers_150000.txt"
                case 8:
                    caminho = "ascending_numbers_200000.txt"
                case _:
                    print("Houve um erro, tente novamente.")
                    break

            return caminho
        
        elif ordem_escolha == '2':
            tamanho = menu_tamanho()
            match tamanho:
                case 0:
                    break
                case 1:
                    caminho = "descending_numbers_100.txt"
                case 2:
                    caminho = "descending_numbers_1000.txt"
                case 3:
                    caminho = "descending_numbers_5000.txt"
                case 4:
                    caminho = "descending_numbers_30000.txt"
                case 5:
                    caminho = "descending_numbers_50000.txt"
                case 6:
                    caminho = "descending_numbers_100000.txt"
                case 7:
                    caminho = "descending_numbers_150000.txt"
                case 8:
                    caminho = "descending_numbers_200000.txt"
                case _:
                    print("Houve um erro, tente novamente.")
                    break

            return caminho
        
        elif ordem_escolha == '3':
            tamanho = menu_tamanho()
            match tamanho:
                case 0:
                    break
                case 1:
                    caminho = "random_numbers_100.txt"
                case 2:
                    caminho = "random_numbers_1000.txt"
                case 3:
                    caminho = "random_numbers_5000.txt"
                case 4:
                    caminho = "random_numbers_30000.txt"
                case 5:
                    caminho = "random_numbers_50000.txt"
                case 6:
                    caminho = "random_numbers_100000.txt"
                case 7:
                    caminho = "random_numbers_150000.txt"
                case 8:
                    caminho = "random_numbers_200000.txt"
                case _:
                    print("Houve um erro, tente novamente.")
                    break
                    

            return caminho
        
        else:
            print("Opção inválida, tente novamente.")

def Bubble(caminho):
    numeros = []
    with open (caminho , 'r' , encoding="utf-8") as arquivo:
        numeros = [linha.strip() for linha in arquivo.readlines()]

    inicio = time.time()

    bubbleSort(numeros)

    fim = time.time()

    tempo_de_execucao = fim - inicio
    print(f"Tempo de execução do Bubble Sort: {tempo_de_execucao}")

def Merge(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo.readlines()]
        lista = []
        for linha in linhas:
            lista.append(linha)

    start = time.time()

    merge_sort(lista, 0, len(lista)-1)

    end = time.time()

    print(f"Tempo de execução do Merge Sort: {end - start}")

if __name__ == "__main__":
    while True:
        print("\n")
        print("Menu de Algoritmos de Ordenação:")
        print("1. Bubble Sort")
        print("2. Merge Sort")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '0':
            break
        elif escolha == '1':
            caminho = menu_ordem()
            Bubble(caminho)

        elif escolha == '2':
            caminho = menu_ordem()
            Merge(caminho)

        else:
            print("Opção inválida, tente novamente.")