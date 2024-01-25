import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from numpy import sin, cos, arccos, pi, exp
import matplotlib.pyplot as plt
import sympy as sym

plt.style.use('ggplot')

# Duota funkcija
def funkcija(x):
    return (exp(-x**2)) * sin(x**2) * (x-3)

# Čiobyševo polinomo formulė
def ciobysevo_daugianaris(x, i):
    return cos(arccos(x) * i)

# Čiobyševo polinomo funkcijos formulė spausdinimui
def sym_ciobysevo_daugianaris(x, i):
    return sym.cos(sym.acos(x) * i)

# Čiobyševo intervalo formulė
def ciobysevo_intervalas(x, a, b):
    return (2 * x - (b + a)) / (b - a)

# Čiobyševo mazgo transformacija
def ciobysevo_mazgas(i, pr, pb, n):
    return ((pb - pr) / 2) * cos(pi * (2 * i + 1) / (2 * n)) + ((pb + pr) / 2)

# Spausdinimo funkcija
def spausdinti_ciobysevo(i, koffs):
    x = sym.Symbol('x')
    koffs = koffs.flatten()
    xc = ciobysevo_intervalas(x, -3, 2)
    for i in range(len(koffs)):
        A = sym_ciobysevo_daugianaris(xc, i)
        if i == 0:
            print(str(koffs[i]) + ' +')
        elif i == 1:
            print(str(koffs[i]) + ' * (' + str(A) + ') +')
        else:
            print(str(koffs[i]) + ' * ' + str(A) + ' +')

print('Pasirinkite taškų išdėstymo tipą:')
print('Tolygiai - tl')
print('Čiobyševo - cb')

n = 15  # interpoliavimo taškų skaičius
i = np.arange(n)

if str(input("Pasirinkta: ")) == "tl":
    x = np.linspace(-3, 2, n).reshape(-1, 1)
    plot_name = 'Taškai tolygiai pasiskirstę'
else:
    x = ciobysevo_mazgas(i, -3, 2, n).reshape(-1, 1)
    plot_name = ' Taškai naudojant Čiobyševo abscises'

int_ciobysevo = ciobysevo_intervalas(x, -3, 2)
cb_daugianaris = ciobysevo_daugianaris(int_ciobysevo, i)
koffs = np.linalg.solve(cb_daugianaris, funkcija(x))

x = np.linspace(-3, 2, 100).reshape(-1, 1)

cb_i_intervalas = ciobysevo_intervalas(x, -3, 2)
cb_i_daugianaris = ciobysevo_daugianaris(cb_i_intervalas, i)
int = np.dot(cb_i_daugianaris, koffs)

plt.plot(x, int, label='Interpoliuota, n=15')
plt.plot(x, funkcija(x), label='Duota')
plt.plot(x, funkcija(x) - int, label='Netiktis')
plt.legend()
plt.title(plot_name)
plt.show()
