import ctypes
import numpy as np
import os

# Get the absolute path to fft.dll
dll_path = os.path.abspath('fft.dll')

# Load the DLL
fft_lib = ctypes.CDLL(dll_path)

# Define the function signature
fft_lib.fft.restype = None
fft_lib.fft.argtypes = [np.ctypeslib.ndpointer(dtype=np.complex128, ndim=1, flags='C_CONTIGUOUS'), ctypes.c_int]

# Define a sample array
N = 8  # Length of the array
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], dtype=np.complex128)

# Perform FFT using the C function
fft_lib.fft(x, N)

# Print the array of complex numbers obtained after FFT
print(x)

