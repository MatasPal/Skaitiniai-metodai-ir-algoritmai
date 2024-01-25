import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import pandas as pd

plt.style.use('ggplot')

def interpoliuoti_globalu(x, y):
    # Surandame interpoliacinį splainą
    spline = UnivariateSpline(x.ravel(), y.ravel(), s=0)

    # Rekonstruojame reikšmes naujuose taškuose
    x_n = np.linspace(x.min(), x.max(), 100)
    y_n = spline(x_n)

    plt.title('Kroatijos emisija 1998-2018 (Globalus)')
    plt.scatter(x, y, label='Esami', color='red')  # Scatter plot for existing data points
    plt.plot(x_n, y_n, 'g-', label='Interpoliuoti')
    plt.legend()
    plt.xticks(np.arange(20), np.arange(1, 21))
    plt.show()

n = 20  # 12 mėnesių
data = pd.read_csv('Croatia_Emissions.csv')
x = data.index.to_numpy().reshape(-1, 1)
y = data.iloc[:, 0].to_numpy().reshape(-1, 1)
del data

interpoliuoti_globalu(x, y)
