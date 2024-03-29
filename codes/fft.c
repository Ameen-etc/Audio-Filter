#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>

#define PI 3.14159265358979323846

// Function to perform FFT
void fft(double complex *x, int N) {
    if (N <= 1) return;

    // Divide the array into even and odd parts
    double complex even[N/2], odd[N/2];
    for (int i = 0; i < N/2; i++) {
        even[i] = x[2*i];
        odd[i] = x[2*i + 1];
    }

    // Recursively compute FFT for even and odd parts
    fft(even, N/2);
    fft(odd, N/2);

    // Combine the results
    for (int k = 0; k < N/2; k++) {
        double complex t = cexp(-2 * PI * I * k / N) * odd[k];
        x[k] = even[k] + t;
        x[k + N/2] = even[k] - t;
    }
}

