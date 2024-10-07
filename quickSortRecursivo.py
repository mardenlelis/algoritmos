def quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Escolhe um pivot
        pivot = arr[len(arr) // 2]
        # Divide o array em sublistas de elementos menores, iguais e maiores que o pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursivamente ordena as sublistas
        return quicksort_recursive(left) + middle + quicksort_recursive(right)

# Exemplo de uso
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort_recursive(arr)
print("Array ordenado recursivamente:", sorted_arr)
