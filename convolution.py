import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 1]
h = [1, 2, 1, -1]

#x = [2, -1, 3, 7, 1, 2, -3]
#h = [1, -1, 2, -2, 4, 1, -2, 5]

def convolve(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1
    y = [0] * len_y

    for i in range(len_y):
        for k in range(len_x):
            if (i - k >= 0 and i - k < len_h):
                y[i] += x[k] * h[i - k]

    return y

plt.figure(figsize=(12,8))


plt.subplot(2, 2, 1)
plt.stem(x)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('x(n)')

plt.subplot(2, 2, 2)
plt.stem(h)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('h(n)')

# Convolution
y = convolve(x, h)

plt.subplot(2, 2, 3)
plt.stem(y)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('y(n) = x(n) * h(n)')

# Crosscorrelation
y = convolve(x, h[::-1])

plt.subplot(2, 2, 4)
plt.stem(y)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('y(n) = x(n) . h(n)')


plt.tight_layout()
plt.show()