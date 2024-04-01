import numpy as np
import matplotlib.pyplot as plt

# Load data from the y_values.dat file
data = np.loadtxt('y_values.dat')
n_values = data[:, 0]
y_values = data[:, 1]

# Values of x(n) from 0 to 5
x_values = [1, 2, 3, 4, 2, 1]

# Plot y(n) and x(n)
plt.figure(figsize=(10, 8))

# Plot x(n) from 0 to 5 in the first subplot
plt.subplot(2, 1, 1)
plt.stem(range(len(x_values)), x_values, basefmt='r-')
plt.xlabel('n')
plt.ylabel('x(n)')

# Plot y(n) in the second subplot
plt.subplot(2, 1, 2)
plt.stem(n_values, y_values, basefmt='r-')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.grid(True)
plt.tight_layout()
plt.show()
