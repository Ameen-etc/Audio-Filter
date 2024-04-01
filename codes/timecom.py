import numpy as np
import time
import matplotlib.pyplot as plt

def convolve_time_complexity(N):
    # Generate random input signals
    x = np.random.rand(N)
    h = np.random.rand(N)
    
    # Measure the execution time for convolution
    start_time = time.time()
    np.convolve(x, h)
    conv_time = time.time() - start_time
    return conv_time

def fft_ifft_time_complexity(N):
    # Generate random input signals
    x = np.random.rand(N)
    h = np.random.rand(N)
    
    # Measure the execution time for FFT and IFFT
    start_time = time.time()
    X = np.fft.fft(x)
    H = np.fft.fft(h)
    y = np.fft.ifft(X * H)
    fft_ifft_time = time.time() - start_time
    return fft_ifft_time

# Define the range of input sizes
input_sizes = [2**i for i in range(2, 16)]

# Measure the execution times for different input sizes
conv_times = [convolve_time_complexity(N) for N in input_sizes]
fft_ifft_times = [fft_ifft_time_complexity(N) for N in input_sizes]

# Plot the results using a stem plot
plt.figure(figsize=(10, 6))
plt.stem(input_sizes, conv_times, label='Convolution', linefmt='b-', markerfmt='bo', basefmt=' ')
plt.stem(input_sizes, fft_ifft_times, label='FFT/IFFT', linefmt='g-', markerfmt='go', basefmt=' ')
plt.xlabel('Input Size (N)')
plt.ylabel('Execution Time (s)')
plt.title('Time Complexity Comparison: Convolution vs. FFT/IFFT')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()

