def merge_sort_iterative(arr):
    # Inicia com o tamanho da sublista sendo 1
    width = 1
    n = len(arr)
    
    while width < n:
        # Itera sobre as sublistas de tamanho 'width'
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            
            # Mescla as duas sublistas
            merged = []
            l = r = 0
            
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            
            # Adiciona os elementos restantes
            merged.extend(left[l:])
            merged.extend(right[r:])
            
            # Coloca a sublista mesclada de volta na lista original
            arr[i:i + 2 * width] = merged
        
        # Dobra o tamanho da sublista a ser mesclada
        width *= 2

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort_iterative(arr)
print("Array ordenado iterativamente:", arr)
