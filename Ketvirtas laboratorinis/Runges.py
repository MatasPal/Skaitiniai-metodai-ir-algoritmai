import numpy as np
import matplotlib.pyplot as plt

def parašiutininko_kritimas(X, t):
    h, v = X
    m1 = 120  # parašiutininko masė (kg)
    m2 = 10   # įrangos masė (kg)
    k1 = 0.25  # oro pasipriešinimo koeficientas laisvo kritimo metu (kg/m)
    k2 = 10    # oro pasipriešinimo koeficientas išskleidus parašiutą (kg/m)
    g = 9.81   # gravitacijos pagreitis (m/s^2)

    if t < 25:
        # Laisvas kritimas iki parašiuto išsiskleidimo
        F = (m1 + m2) * g - k1 * v**2 * np.sign(v)
    else:
        # Parašiutas išsiskleidęs
        F = (m1 + m2) * g - k2 * v**2 * np.sign(v)

    dhdt = -v
    dvdt = F / (m1 + m2)

    return np.array([dhdt, dvdt])

def runge_kutta_4(func, y0, t):
    N = len(t)
    y = np.zeros((len(y0), N))
    y[:, 0] = y0

    for i in range(N - 1):
        h = t[i + 1] - t[i]
        k1 = h * func(y[:, i], t[i])
        k2 = h * func(y[:, i] + k1 / 2, t[i] + h / 2)
        k3 = h * func(y[:, i] + k2 / 2, t[i] + h / 2)
        k4 = h * func(y[:, i] + k3, t[i] + h)
        y[:, i + 1] = y[:, i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return y

# Laiko nustatymai
viso_laikas = 170  # Visas skaičiavimo laikas (s)
dt_values = [0.01, 0.1, 0.5, 1.2]  # Laiko žingsniai Eulerio metodu

# Pradinės sąlygos
h0 = 2800  # Pradinis aukštis (m)
v0 = 0     # Pradinis greitis (m/s)

# Braižome rezultatus su skirtingais laiko žingsniais
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

for dt in dt_values:
    # Laiko vektorius
    t = np.arange(0, viso_laikas, dt)

    # Skaičiavimas naudojant Rungės-Kutos metodą
    rezultatai_rk4 = runge_kutta_4(parašiutininko_kritimas, [h0, v0], t)

    # Analizuojame rezultatus
    pasiekimo_momento_indeksas = np.argmax(rezultatai_rk4[0] <= 0)  # Indeksas, kai aukštis tampa neigiamas
    pasiekimo_laikas = t[pasiekimo_momento_indeksas]
    pasiekimo_greitis = rezultatai_rk4[1, pasiekimo_momento_indeksas]

    išskleidimo_indeksas = np.argmax((t >= 25) & (rezultatai_rk4[0] > 0))  # Indeksas, kai parašiutas išsiskleidžia
    išskleidimo_laikas = t[išskleidimo_indeksas]
    išskleidimo_aukštis = rezultatai_rk4[0, išskleidimo_indeksas]

    # Braižome rezultatus aukščio grafike
    ax1.plot(t, rezultatai_rk4[0, :], label=f'Aukštis (dt = {dt:.2f})')

    # Braižome rezultatus greičio grafike
    ax2.plot(t, rezultatai_rk4[1, :], label=f'Greitis (dt = {dt:.2f})')

# Plot nustatymai aukščio grafikui
ax1.set_xlabel('Laikas (s)')
ax1.set_ylabel('Aukštis (m)')
ax1.legend()

# Plot nustatymai greičio grafikui
ax2.set_xlabel('Laikas (s)')
ax2.set_ylabel('Greitis (m/s)')
ax2.legend()

plt.tight_layout()
plt.show()
