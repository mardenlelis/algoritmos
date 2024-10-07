def torre_de_hanoi(n, origem, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    # Mover n-1 discos da origem para o auxiliar
    torre_de_hanoi(n-1, origem, destino, auxiliar)
    # Mover o disco restante da origem para o destino
    print(f"Mover disco {n} de {origem} para {destino}")
    # Mover n-1 discos do auxiliar para o destino
    torre_de_hanoi(n-1, auxiliar, origem, destino)

# Exemplo de uso: mover 3 discos da torre A para a torre C usando a torre B como auxiliar
n = 5
torre_de_hanoi(n, 'A', 'B', 'C')
