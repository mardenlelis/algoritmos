def bubbleSort(A, n):
    if n == 1:
        return
    for i in range(n-1):
        if (A[i] > A[i+1]):
            aux = A[i]
            A[i] = A[i+1]
            A[i+1] = aux
    bubbleSort(A, n-1)

if __name__ == '__main__':
    A = [21, 4, 67, 8, 57, 90, 31]
    n = len(A)
    print(f"Lista original: {A}")
    bubbleSort(A, n)
    print(f"Lista ordenada: {A}")
