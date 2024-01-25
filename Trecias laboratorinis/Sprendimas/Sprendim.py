import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

def f(x):
    return np.exp(-x**2) * np.sin(x**2) * (x - 3)

def chebyshev_nodes(a, b, n):
    k = np.arange(1, n + 1)
    nodes = 0.5 * (a + b) + 0.5 * (b - a) * np.cos((2 * k - 1) * np.pi / (2 * n))
    return nodes

def chebyshev_interpolation(x, y, n):
    nodes = chebyshev_nodes(min(x), max(x), n)
    A = np.vander(nodes, increasing=True)
    coefficients = np.linalg.solve(A, y)
    return np.vander(x, increasing=True)[:,:n] @ coefficients[:n]  # Pakeitimas: Truncate the matrix and coefficients

# Generuojame duotąją funkciją
x_exact = np.linspace(-3, 2, 1000)
y_exact = f(x_exact)

# Tolygiai pasiskirstyti Čiobyševo taškai
n_uniform = 15
x_uniform = np.linspace(-3, 2, n_uniform)
y_uniform = f(x_uniform)
y_interpolated_uniform = chebyshev_interpolation(x_exact, y_uniform, n_uniform)

# Čiobyševo abscises
n_chebyshev = 15
x_chebyshev = chebyshev_nodes(-3, 2, n_chebyshev)
y_chebyshev = f(x_chebyshev)
y_interpolated_chebyshev = chebyshev_interpolation(x_exact, y_chebyshev, n_chebyshev)

# Netiktis (skirtumas tarp duotosios funkcijos ir interpoliuojančios funkcijos)
y_residual_uniform = y_exact - y_interpolated_uniform
y_residual_chebyshev = y_exact - y_interpolated_chebyshev

# Braižome grafikus
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_exact, y_exact, label='Duota funkcija')
plt.plot(x_exact, y_interpolated_uniform, label=f'Interpoliacija (tolygiai), n={n_uniform}')
plt.plot(x_uniform, y_uniform, 'ro', label='Interpoliacijos taškai (tolygiai)')
plt.plot(x_exact, y_residual_uniform, label=f'Netiktis (tolygiai), n={n_uniform}')
plt.title('Interpoliacija (tolygiai)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_exact, y_exact, label='Duota funkcija')
plt.plot(x_exact, y_interpolated_chebyshev, label=f'Interpoliacija (Čiobyševo), n={n_chebyshev}')
plt.plot(x_chebyshev, y_chebyshev, 'ro', label='Interpoliacijos taškai (Čiobyševo)')
plt.plot(x_exact, y_residual_chebyshev, label=f'Netiktis (Čiobyševo), n={n_chebyshev}')
plt.title('Interpoliacija (Čiobyševo)')
plt.legend()

plt.tight_layout()
plt.show()
