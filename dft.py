import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

N = 512
t = np.arange(0, 1, 1/N) # fs = 512
x = 10 * np.sin(2 * np.pi * 40 * t) + 20 * np.sin(2 * np.pi * 80 * t) + 40 * np.sin(2 * np.pi * 160 * t)

def dft(x_n):
    N = len(x)
    X_m = np.zeros(N, dtype=np.complex128)
    for m in range(N):
        for n in range(N):
            X_m[m] += x_n[n] * np.exp(-2j * np.pi * m * n / N)

    return X_m

def phase(X_m):
    X_phase = []
    for z in X_m:
        phase = cmath.phase(round(z.real) + round(z.imag) * 1j)
        X_phase.append(math.degrees(phase))

    return X_phase

def idft(X):
    N = len(X)
    x = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        for m in range(N):
            x[n] += X[m] * np.exp(2j * np.pi * m * n / N)
        x[n] = x[n]/N
    return x

X_m = dft(x)

plt.figure(figsize=(10, 4))

plt.subplot(2, 2, 1)
plt.stem(np.abs(X_m))
plt.xlabel('m')
plt.ylabel('x(m)')
plt.title('Magnitude Spectrum')

X_phase = phase(X_m)

plt.subplot(2, 2, 2)
plt.stem(X_phase)
plt.xlabel('m')
plt.ylabel('Angle (in Degrees)')
plt.title('Phase Spectrum')

x_n = idft(X_m)
plt.subplot(2, 2, 3)
plt.stem(x_n)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Reconstructed DFT')

plt.tight_layout()
plt.show()