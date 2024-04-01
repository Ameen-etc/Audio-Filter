import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Sampling frequency of Input signal
sample_freq = 44100

# Cutoff frequency (example value)
cutoff_freq = 4000.0  # For example, 4 kHz

# Order of the Butterworth filter
order = 4

# Digital frequency
Wn = 2 * cutoff_freq / sample_freq

# Design Butterworth filter and obtain coefficients
b, a = signal.butter(order, Wn, 'low')

# Define the frequency response function
def frequency_response(b, a, num_points=8000):
    w = np.linspace(0, np.pi, num_points)
    H_z = np.polyval(b[::-1], np.exp(1j * w)) / np.polyval(a[::-1], np.exp(1j * w))
    return w, H_z

# Compute the frequency response of the filter
w, H_z = frequency_response(b, a)

# Plot the frequency response (magnitude)
plt.figure(figsize=(10, 6))
plt.plot(w, np.abs(H_z), 'b')
plt.title('Discrete Time Filter')
plt.xlabel('f')
plt.ylabel('|H(e^(jw))|')
plt.grid()
plt.show()

