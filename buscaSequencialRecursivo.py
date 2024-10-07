def buscaSequencial(x, A, n):
    if n == 0:
        return -1 
    if (A[n-1] == x):
        return n-1 
    return buscaSequencial(x, A, n-1) 

if __name__ == '__main__':
    A = [21, 4, 67, 8, 57, 90, 31]
    x = 8
    n = len(A)
    resultado = buscaSequencial(x, A, n)

    if resultado == -1:
        print(f"Elemento {x} não encontrado")
    else:
        print(f"Elemento {x} encontrado na posição: {resultado}")