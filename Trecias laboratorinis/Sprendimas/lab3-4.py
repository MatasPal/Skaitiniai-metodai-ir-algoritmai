import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from interpolation import parametric_interpolation, hermite_interpolation_spline
from lab3_4_data import x_range, y_range
import time

n = 1500  # Number of interpolation points
step = 0.1# Graph's precision

# Measure time before interpolation
start_time = time.time()

# Reducing interpolation points to selected
t = range(n + 1)
x_range = x_range[::(2359 // n)]
y_range = y_range[::(2359 // n)]

ff = hermite_interpolation_spline(t, x_range)
ff2 = hermite_interpolation_spline(t, y_range)

xx, yy = parametric_interpolation(ff, ff2, np.arange(0, n, step))

end_time = time.time()
# Plot country borders as a line
plt.plot(x_range, y_range, 'r-', label="Šalies ribos")

# Scatter plot for interpolation points
plt.scatter(x_range, y_range, color='blue',  marker='o', label=f"{n} Aproksimavimo taškai")

plt.title('Kroatija')
plt.legend()
plt.show()

# Print the elapsed time
elapsed_time = end_time - start_time
print(f"Aproksimavimas užtruko {elapsed_time:.4f} sekundžių.")