import numpy as np
import matplotlib.pyplot as plt

N = 20
x = np.ones(N)
n = np.arange(0,N)

plt.figure(figsize=(12, 8.5))

# Unit Step Sequence
plt.subplot(3, 2, 1)
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Unit Step Sequence')

# Unit Ramp Signal
plt.subplot(3, 2, 2)
plt.stem(n,n)
plt.xlabel('n')
plt.ylabel('Ur(n)')
plt.title('Unit Ramp Signal')
plt.grid()

# Exponential Signal
a = 0.575**n
plt.subplot(3, 2, 3)
plt.stem(n,a)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Exponential Signal')
plt.grid()

# Cosine signal
point = np.linspace(0, 2*np.pi, 100)
plt.subplot(3, 2, 4)
plt.stem(point, np.cos(point))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Cosine wave')
plt.grid()

# Sine Signal
plt.subplot(3, 2, 5)
plt.stem(point, np.sin(point))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Sine wave')

plt.grid()
plt.tight_layout()
plt.show()