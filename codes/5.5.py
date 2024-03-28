import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt

N = 14
n = np.arange(N)

# Define impulse response h(n)
hn = (-1/2)**n
hn = np.pad(hn, (0, N - len(hn)), 'constant')

# Define input signal x(n)
xtemp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(xtemp, (0, N - len(xtemp)), 'constant')

# Compute DFT matrix
dft_matrix = np.fft.fft(np.eye(N))

# Compute DFT of x and h using DFT matrix
X = x @ dft_matrix
H = hn @ dft_matrix

# Compute frequency response Y = H * X
Y = H * X

# Compute inverse DFT of Y to obtain y(n)
y = np.fft.ifft(Y).real

# Plot the output signal
plt.stem(range(N), y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.title('Output Signal y(n)')
plt.grid(True)
plt.show()
