import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#sampling frequency from the audio file
sampl_freq=44100
T = 1.0/sampl_freq
#order of the filter
order=4

#cutoff frquency 
cutoff_freq=4000.0 

#digital frequency
Wn=2*cutoff_freq/sampl_freq  


# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low')

# Bilinear Transform
def H(s):
    num = np.polyval(b, ((1 + s * (T / 2)) / (1 - s * (T / 2))) ** (-1))
    den = np.polyval(a, ((1 + s * (T / 2)) / (1 - s * (T / 2))) ** (-1))
    H = num / den
    return H

# Calculate poles and zeros of H(s)
_, poles, zeros = signal.tf2zpk(b, a)

# Plot pole-zero plot
plt.figure(figsize=(8, 6))
plt.scatter(poles.real, poles.imag, marker='x', color='red', label='Poles')
plt.scatter(zeros.real, zeros.imag, marker='o', color='blue', label='Zeros')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole-Zero Plot of H(s)')
plt.legend()
plt.grid()
plt.show()
