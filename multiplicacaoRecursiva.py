def multiplica(y, z):
    if z == 0:
        return 0
    elif z % 2 == 1:  # z é ímpar
        return multiplica(2 * y, z // 2) + y
    else:
        return multiplica(2 * y, z // 2)

# Testando a função com alguns exemplos:
resultado = multiplica(5, 3)
print(f"Resultado de multiplica(5, 3): {resultado}")

resultado = multiplica(6, 4)
print(f"Resultado de multiplica(6, 4): {resultado}")

resultado = multiplica(10, 0)
print(f"Resultado de multiplica(10, 0): {resultado}")
