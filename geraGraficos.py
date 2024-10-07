import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo de n
n = np.linspace(1, 10, 400)

# Definindo as funções
f_sqrt_n = np.sqrt(n)
f_n = n
f_n_log_n = n * np.log(n)
f_n2 = n ** 2
f_n3 = n ** 3
f_floor_n = np.floor(n)
f_ceil_n = np.ceil(n)

# Plotando os gráficos
fig, axs = plt.subplots(4, 2, figsize=(12, 16))
fig.tight_layout(pad=4.0)

# f(n) = sqrt(n)
axs[0, 0].plot(n, f_sqrt_n, label=r'$f(n) = \sqrt{n}$')
axs[0, 0].set_title(r'$f(n) = \sqrt{n}$')
axs[0, 0].grid(True)

# f(n) = n
axs[0, 1].plot(n, f_n, label=r'$f(n) = n$')
axs[0, 1].set_title(r'$f(n) = n$')
axs[0, 1].grid(True)

# f(n) = n log n
axs[1, 0].plot(n, f_n_log_n, label=r'$f(n) = n \log n$')
axs[1, 0].set_title(r'$f(n) = n \log n$')
axs[1, 0].grid(True)

# f(n) = n^2
axs[1, 1].plot(n, f_n2, label=r'$f(n) = n^2$')
axs[1, 1].set_title(r'$f(n) = n^2$')
axs[1, 1].grid(True)

# f(n) = n^3
axs[2, 0].plot(n, f_n3, label=r'$f(n) = n^3$')
axs[2, 0].set_title(r'$f(n) = n^3$')
axs[2, 0].grid(True)

# f(n) = floor(n)
axs[2, 1].step(n, f_floor_n, label=r'$f(n) = \lfloor n \rfloor$', where='post')
axs[2, 1].set_title(r'$f(n) = \lfloor n \rfloor$')
axs[2, 1].grid(True)

# f(n) = ceil(n)
axs[3, 0].step(n, f_ceil_n, label=r'$f(n) = \lceil n \rceil$', where='post')
axs[3, 0].set_title(r'$f(n) = \lceil n \rceil$')
axs[3, 0].grid(True)

# Removendo gráfico vazio
fig.delaxes(axs[3, 1])

# Exibir os gráficos
plt.show()
