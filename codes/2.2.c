#include <stdio.h>

#define N 20

void calculateY() {
    double y[N + 1] = {0}; // Initializing y with zeros
    double x[N + 3] = {0, 0, 1, 2, 3, 4, 2, 1, 0}; // Input signal x with additional elements for x[-1] and x[-2]

    // Calculate initial conditions
    y[0] = x[2] + x[0];
    y[1] = x[3] + x[1] - 0.5 * y[0];

    // Calculate y using the difference equation
    for (int n = 2; n <= N; n++) {
        y[n] = -0.5 * y[n - 1] + x[n + 2] + x[n];
    }

    // Store values of y(n) in a dat file
    FILE *fp = fopen("y_values.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    for (int n = 0; n <= N; n++) {
        fprintf(fp, "%d %f\n", n, y[n]);
    }

    fclose(fp);
}

int main() {
    calculateY();
    return 0;
}
