def bublleSort(A, n):
    for j in range(n-1, 0, -1):
        for i in range(j):
            if (A[i] > A[i+1]):
                aux = A[i]
                A[i] = A[i+1]
                A[i+1] = aux

if __name__ == '__main__':
    A = [21, 4, 67, 8, 57, 90, 31]
    n = len(A)
    print(f"Lista original: {A}")
    bublleSort(A, n)
    print(f"Lista ordenada: {A}")
        