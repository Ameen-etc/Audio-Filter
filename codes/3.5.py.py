import numpy as np
import matplotlib.pyplot as plt

# Define the transfer function
def H(w):
    numerator = 1 + np.exp(-2j * w)
    denominator = 1 + 0.5 * np.exp(-1j * w)
    return numerator / denominator

# Generate a range of frequencies from 0 to pi
omega = np.linspace(-10, 10, 1000)

# Evaluate the transfer function for each frequency
H_values = H(omega)

# Plot the magnitude of the transfer function
plt.figure(figsize=(8, 6))
plt.plot(omega, np.abs(H_values))
plt.title('Magnitude of Transfer Function $|H(e^{j\omega})|$')
plt.xlabel('Frequency (radians)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
