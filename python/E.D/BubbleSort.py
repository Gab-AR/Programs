def bubble_sort(lista):
    n = len(lista)
    # Percorre toda a lista
    for i in range(n):
        # Últimos i elementos já estão na posição correta
        for j in range(0, n - i - 1):
            # Troca se o elemento atual é maior que o próximo
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Exemplo de uso
letras = ['W', 'T', 'R', 'A', 'N', 'S', 'F', 'O', 'R', 'M', 'E', 'R', 'S', 'U', 'F', 'P', 'I']
ordenado = bubble_sort(letras)
print("Sequência ordenada:", ordenado)