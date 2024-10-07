def selection_sort_recursive(arr, i=0):
    n = len(arr)
    # Caso base: se i for igual ao tamanho do array, o array já está ordenado
    if i == n:
        return

    # Encontre o índice do menor elemento no restante do array
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    
    # Troca o menor elemento encontrado com o elemento na posição i
    arr[i], arr[min_index] = arr[min_index], arr[i]

    # Chama a função recursivamente para o próximo índice
    selection_sort_recursive(arr, i + 1)

# Exemplo de uso
arr = [64, 25, 12, 22, 11]
selection_sort_recursive(arr)
print("Array ordenado recursivamente:", arr)
