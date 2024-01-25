import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')


def kelti(x, laipsnis):
    x = x.flatten()  # iš 2d į 1d
    return np.array([x ** i for i in range(laipsnis)]).T.astype(float)  # skaičius pakeliamas tam tikru laipsniu

def b(x, koffs):  # aproksimavimui x pakelti ir su koffu sudaugint
    koffs = koffs.flatten()  # iš 2d į 1d
    ats = 0
    for i in range(len(koffs)):
        ats += koffs[i] * x ** i
        print(f'{koffs[i]} * x ^ {i} +')
    return ats

laipsnis = int(input('Daugianario laipsnis: '))
laipsnis += 1
duomenys = pd.read_csv('Croatia_Emissions.csv')
x = duomenys.index.to_numpy().reshape(-1, 1)  # indeksai/mėnesiai
y = duomenys.iloc[:, 0].to_numpy().reshape(-1, 1)  # temperatūros

G = kelti(x, laipsnis)
koffs = np.linalg.solve(G.T.dot(G), G.T.dot(y))  # išsprendžia lygčių sistema

xx = np.arange(0, 21, 0.01).reshape(-1, 1)  # į 2d

plt.plot(x, y, 'D', label=f'esami = {len(x)}')
plt.plot(xx, b(xx, koffs), 'g-', label=f'aproksimavimas = {laipsnis-1}')
plt.xticks(np.arange(22), np.arange(1, 23))
plt.title('Kroatijos emisija 1998-2018')
plt.legend()
plt.show()
