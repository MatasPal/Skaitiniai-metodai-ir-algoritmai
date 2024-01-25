import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def parašiutininko_kritimas(t, X):
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

    return [dhdt, dvdt]

# Laiko nustatymai
viso_laikas = 146  # Visas skaičiavimo laikas (s)

# Pradinės sąlygos
h0 = 2800  # Pradinis aukštis (m)
v0 = 0     # Pradinis greitis (m/s)

# Laiko vektorius
t_span = (0, viso_laikas)

# Skaičiavimas naudojant solve_ivp
rezultatai_ivp = solve_ivp(parašiutininko_kritimas, t_span, [h0, v0], t_eval=np.linspace(0, viso_laikas, 1000), method='RK45')

# Analizuojame rezultatus
pasiekimo_momento_indeksas = np.argmax(rezultatai_ivp.y[0] <= 0)  # Indeksas, kai aukštis tampa neigiamas
pasiekimo_laikas = rezultatai_ivp.t[pasiekimo_momento_indeksas]
pasiekimo_greitis = rezultatai_ivp.y[1, pasiekimo_momento_indeksas]

išskleidimo_indeksas = np.argmax((rezultatai_ivp.t >= 25) & (rezultatai_ivp.y[0] > 0))  # Indeksas, kai parašiutas išsiskleidžia
išskleidimo_laikas = rezultatai_ivp.t[išskleidimo_indeksas]
išskleidimo_aukštis = rezultatai_ivp.y[0, išskleidimo_indeksas]

# Spausdiname rezultatus
print(f"Parašiutininkas pasiekia žemę laiko t = {pasiekimo_laikas:.2f} s metu su greičiu {pasiekimo_greitis:.2f} m/s.")
print(f"Parašiutas išsiskleidžiamas laiko t = {išskleidimo_laikas:.2f} s metu, esant aukštyje {išskleidimo_aukštis:.2f} m.")

# Braižome rezultatus
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Aukščio grafikas
ax1.plot(rezultatai_ivp.t, rezultatai_ivp.y[0], label='Aukštis (solve_ivp)')
ax1.set_xlabel('Laikas (s)')
ax1.set_ylabel('Aukštis (m)')
ax1.legend()

# Greičio grafikas
ax2.plot(rezultatai_ivp.t, rezultatai_ivp.y[1], label='Greitis (solve_ivp)')
ax2.set_xlabel('Laikas (s)')
ax2.set_ylabel('Greitis (m/s)')
ax2.legend()

plt.tight_layout()
plt.show()
