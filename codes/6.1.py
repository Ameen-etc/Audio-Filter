import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal

# Read the first .wav file
input_signal_1, fs_1 = sf.read('Tomar_ Khola_Hawa.wav')

# Read the second .wav file
input_signal_2, fs_2 = sf.read('Tomar_Khola_Hawa_NR.wav')

# Select the desired segment (e.g., first 10 seconds) for both signals
duration = 3  # in seconds
num_samples = int(duration * fs_1)
input_signal_segment_1 = input_signal_1[:num_samples]
input_signal_segment_2 = input_signal_2[:num_samples]

# Order of the filter
order = 4

# Cutoff frequency 4kHz
cutoff_freq = 4000.0

# Design Butterworth filter and obtain coefficients
b, a = signal.butter(order, cutoff_freq / (fs_1 / 2), 'low')

# Apply Z-transform to input signal segment 1
X_z_1 = np.fft.fft(input_signal_segment_1)

# Frequency axis for evaluating H(z)
omega = np.linspace(0, 2*np.pi, len(X_z_1))

# Evaluate H(z) at each frequency
H_z = np.polyval(b[::-1], np.exp(1j * omega)) / np.polyval(a[::-1], np.exp(1j * omega))

# Apply filter in Z-domain for input signal segment 1
Y_z_1 = X_z_1 * H_z

# Apply inverse Z-transform to obtain filtered output for input signal segment 1
output_signal_segment_1 = np.fft.ifft(Y_z_1).real

# Plot the output signal (scatter plot) for input signal segment 2
plt.figure(figsize=(10, 4))
plt.scatter(range(len(input_signal_segment_2)), input_signal_segment_2, s=1, marker='.', label='Originally Filterred')

plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the input signal segment 1
plt.scatter(range(len(output_signal_segment_1)), output_signal_segment_1, s=1, marker='.', label='Manually Filtered')
plt.legend()

plt.savefig('manualvsfun.png')

