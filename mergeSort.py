def merge_sort(A, p, r): 
    if p < r:  #
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    L = A[p:q + 1]
    R = A[q + 1:r + 1]
    i = j = 0
    k = p
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

# Exemplo de uso:
A = [38, 27, 43, 3, 9, 82, 10]
n = len(A)
merge_sort(A, 0, n - 1)
print("Array ordenado:", A)
