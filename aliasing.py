import numpy as np
import matplotlib.pyplot as plt

# sin(2*pi*10t)
# sin(2*pi*50t)

t = np.arange(0,1,0.001)
x1 = np.sin(2*np.pi*10*t)

plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.plot(x1)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('x(t) = sin(2π.10t)')
plt.grid()

x2 = np.sin(2*np.pi*50*t)

plt.subplot(2,2,2)
plt.plot(x2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('x(t) = sin(2π.50t)')
plt.grid()

fs = 40
t = np.arange(0,1,1/fs)

x1 = np.sin(2*np.pi*10*t)

plt.subplot(2,2,3)
plt.stem(x1)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('x(t) = sin(2π.10/40n)')
plt.grid()

x2 = np.sin(2*np.pi*50*t)

plt.subplot(2,2,4)
plt.stem(x2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('x(t) = sin(2π.50/40n)')
plt.grid()


plt.tight_layout()
plt.show()