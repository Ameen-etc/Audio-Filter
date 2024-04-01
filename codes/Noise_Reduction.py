import soundfile as sf
from scipy import signal

# Read .wav file
input_signal, fs = sf.read('Tomar_ Khola_Hawa.wav')

# Sampling frequency of Input signal
sample_freq = fs

# Order of the filter
order = 4

# Cutoff frequency 4kHz
cutoff_freq = 4000.0

# Digital frequency
Wn = 2 * cutoff_freq / sample_freq

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low')

# Filter the input signal with Butterworth filter
output_signal = signal.filtfilt(b, a, input_signal, padlen=1)

# Write the output signal into .wav file
sf.write('Tomar_Khola_Hawa_NR.wav', output_signal, fs)

