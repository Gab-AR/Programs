import time
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
if __name__ == '__main__':
    tempos = []
    for i in range(10):
        nomes = []
        arq = "ascending_numbers_100000.txt"
        with open (arq , 'r' , encoding="utf-8") as arquivo:
            nomes = [linha.strip() for linha in arquivo.readlines()]

        inicio = time.time()

        bubbleSort(nomes)

        fim = time.time()

        tempo_de_execucao = fim - inicio
        tempos.append(tempo_de_execucao)
        print(tempos[i])

        