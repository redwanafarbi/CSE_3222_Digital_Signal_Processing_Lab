import numpy as np
import matplotlib.pyplot as plt

b = [0.1, 0.2, 0.3] # Numerator coefficients
a = [1, -0.5, 0.25] # Denominator coefficients

n = 8000
w = np.linspace(0, np.pi, n)
H = np.zeros(n, dtype=complex)

for i in range(n):
    z = np.exp(1j * w[i]) # z = e^(jw)
    numerator = 0 + 0j
    denominator = 0 + 0j
    for k in range(len(b)):
        numerator += b[k] * (z ** -k)
    for k in range(len(a)):
        denominator += a[k] * (z ** -k)
    H[i] = numerator / denominator

magnitude = np.abs(H)
phase = np.angle(H)

plt.figure(figsize=(8, 4))

plt.subplot(2, 1, 1)
plt.plot(w, magnitude)
plt.xlabel('Frequency (in radians/sample)')
plt.ylabel('Magnitude of H')
plt.title('Magnitude Response')

plt.subplot(2, 1, 2)
plt.plot(w, phase)
plt.xlabel('Frequency (in radians/sample)')
plt.ylabel('Phase (in radians)')
plt.title('Phase Response')


plt.tight_layout()
plt.show()