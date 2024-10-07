
def buscaSequencial(x, A, n):
    k = n -1
    while k >= 0 and A[k] != x:
        k -= 1
    return k


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 29, 8, 9, 10]
    x = 29
    n = len(A)
    resultado = buscaSequencial(x, A, n)

    if resultado == -1:
        print(f"Elemento {x} não encontrado.")
    else:
         print(f"Elemento {x} encontrado no índice {resultado}.")
