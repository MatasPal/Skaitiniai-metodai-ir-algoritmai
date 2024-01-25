import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend (or another backend that works for you)
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import pandas as pd

plt.style.use('ggplot')

def interpoliuoti_splaina(x, y):
    spline = CubicSpline(x.flatten(), y.flatten())

    x_n = np.linspace(x.min(), x.max(), 100)
    y_n = spline(x_n)

    plt.title('Kroatijos emisija 1998-2018')
    plt.scatter(x, y, label='Esami', color='red')  # Scatter plot for existing data points
    plt.plot(x_n, y_n, 'g-', label='Interpoliuoti')
    plt.legend()
    plt.xticks(np.arange(20), np.arange(1, 21))
    plt.show()

n = 20  # 20 metu
data = pd.read_csv('Croatia_Emissions.csv')
x = data.index.to_numpy().reshape(-1, 1)  # Index'ai į 2D dimensiją stulpelis
y = data.iloc[:, 0].to_numpy().reshape(-1, 1)  # Temperatūros į 2D dimensiją stulpelis
del data

interpoliuoti_splaina(x, y)
