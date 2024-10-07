def encontra_majoritario(A):
    candidato = A[0]
    contador = 1
    
    # Fase 1: Encontrar o candidato
    for i in range(1, len(A)):
        if contador == 0:
            candidato = A[i]
            contador = 1
        elif A[i] == candidato:
            contador += 1
        else:
            contador -= 1
    
    # Fase 2: Verificar se o candidato é majoritário
    contador = 0
    for i in A:
        if i == candidato:
            contador += 1
    
    if contador > len(A) // 2:
        return candidato  # Há um elemento majoritário
    else:
        return -1  # Não há elemento majoritário

# Testando a função
A = [3, 3, 4, 2, 4, 4, 2, 4, 4]
resultado = encontra_majoritario(A)
resultado
