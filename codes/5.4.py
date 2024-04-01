import numpy as np
import matplotlib.pyplot as plt

N = 14
n = np.arange(N)
fn = (-1/2)**n
hn1 = np.pad(fn, (0, 2), 'constant', constant_values=(0))
hn2 = np.pad(fn, (2, 0), 'constant', constant_values=(0))
h = hn1 + hn2

xtemp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(xtemp, (0, 8), 'constant', constant_values=(0))

X = np.fft.fft(x, n=N)
H = np.fft.fft(h, n=N)

Y = X * H

y = np.fft.ifft(Y)

y = np.real(y) / N

# Plot
plt.stem(range(0, N), y)
plt.title('Filter Output using FFT and IFFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.show()
