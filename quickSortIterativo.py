def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # Índice do menor elemento
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_iterative(arr):
    n = len(arr)
    # Cria uma pilha para simular as chamadas recursivas
    stack = [(0, n - 1)]
    
    # Processa os elementos na pilha
    while stack:
        low, high = stack.pop()
        
        if low < high:
            # Realiza a partição
            pi = partition(arr, low, high)
            
            # Empurra os subarrays resultantes na pilha
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

# Exemplo de uso
arr = [10, 7, 8, 9, 1, 5]
quicksort_iterative(arr)
print("Array ordenado iterativamente:", arr)
