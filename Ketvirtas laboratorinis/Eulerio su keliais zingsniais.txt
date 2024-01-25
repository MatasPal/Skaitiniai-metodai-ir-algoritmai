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

# Laiko nustatymai
viso_laikas = 146  # Visas skaičiavimo laikas (s)
dt_values = [0.01, 0.05, 0.1, 0.15]  # Laiko žingsniai Eulerio metodu

# Pradinės sąlygos
h0 = 2800  # Pradinis aukštis (m)
v0 = 0     # Pradinis greitis (m/s)

# Braižome rezultatus su skirtingais laiko žingsniais
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

for dt in dt_values:
    # Rezultatų masyvas
    N = int(viso_laikas / dt) + 1
    t = np.linspace(0, viso_laikas, N)
    rezultatas = np.zeros([2, N])
    rezultatas[:, 0] = np.array([h0, v0])

    # Skaičiavimas naudojant Eulerio metodą
    for i in range(N - 1):
        išvestinė = parašiutininko_kritimas(rezultatas[:, i], t[i])
        rezultatas[:, i + 1] = rezultatas[:, i] + išvestinė * dt

    # Analizuojame rezultatus
    pasiekimo_momento_indeksas = np.argmax(rezultatas[0] <= 0)  # Indeksas, kai aukštis tampa neigiamas
    pasiekimo_laikas = t[pasiekimo_momento_indeksas]
    pasiekimo_greitis = rezultatas[1, pasiekimo_momento_indeksas]

    išskleidimo_indeksas = np.argmax((t >= 25) & (rezultatas[0] > 0))  # Indeksas, kai parašiutas išsiskleidžia
    išskleidimo_laikas = t[išskleidimo_indeksas]
    išskleidimo_aukštis = rezultatas[0, išskleidimo_indeksas]

    # Spausdiname rezultatus
    print(f"Su dt = {dt:.2f}:")
    print(f"Parašiutininkas paliečia žemę laiko t = {pasiekimo_laikas:.2f} s su greičiu {pasiekimo_greitis:.2f} m/s.")
    print(f"Parašiutas išskleidžiamas laiko t = {išskleidimo_laikas:.2f} s metu, esant aukštyje {išskleidimo_aukštis:.2f} m.\n")

    # Braižome rezultatus
    ax1.plot(t, rezultatas[0, :], label=f'Žingsnis (dt = {dt:.2f})')

    # Grafikas greičiui
    ax2.plot(t, rezultatas[1, :], label=f'Žingsnis (dt = {dt:.2f})')

# Plot nustatymai
ax1.set_xlabel('Laikas (s)')
ax1.set_ylabel('Aukštis (m)')
ax1.legend()

# Plot nustatymai
ax2.set_xlabel('Laikas (s)')
ax2.set_ylabel('Greitis (m/s)')
ax2.legend()

plt.tight_layout()
plt.show()
