def selection_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        # Assume que o menor elemento está na posição i
        min_index = i
        # Encontre o índice do menor elemento no restante do array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Troca o menor elemento encontrado com o elemento na posição i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso
arr = [64, 25, 12, 22, 11]
selection_sort_iterative(arr)
print("Array ordenado iterativamente:", arr)
