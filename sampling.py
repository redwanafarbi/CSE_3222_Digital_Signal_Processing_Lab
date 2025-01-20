import numpy as np
import matplotlib.pyplot as plt

points = np.arange(0, 0.25, 0.00001)

signal = 10 * np.sin(2 * np.pi * 40* points) + 20 * np.sin(2 * np.pi * 80 * points) + 40 * np.sin(2*np.pi*160 * points)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(points, signal)
plt.xlabel('Time')
plt.ylabel('amplitude')
plt.title('Composite Signal')
plt.grid()

# Nyquist rate
nr = 320
nr_point = np.arange(0, 0.25, 1/nr)
signal_sample_at_nr = 10 * np.sin(2 * np.pi * 40* nr_point) + 20 * np.sin(2 * np.pi * 80 * nr_point) + 40 * np.sin(2*np.pi*160 * nr_point)

plt.subplot(2, 2, 2)
plt.stem(nr_point, signal_sample_at_nr)
plt.xlabel('Time')
plt.ylabel('amplitude')
plt.title('Composite Signal after Sampling At Nyquist Rate')
plt.grid()

# Up Sampling
up_Fs = 450
up_points = np.arange(0,0.25,1/up_Fs)
signal_after_upSampling = 10 * np.sin(2 * np.pi * 40* up_points) + 20 * np.sin(2 * np.pi * 80 * up_points) + 40 * np.sin(2*np.pi*160 * up_points)

plt.subplot(2, 2, 3)
plt.stem(up_points, signal_after_upSampling)
plt.xlabel('Time')
plt.ylabel('amplitude')
plt.title('Composite Signal after Up Sampling')
plt.grid()

# Down Sampling
down_Fs = 20
down_points = np.arange(0,0.25,1/down_Fs)
signal_after_downSampling = 10 * np.sin(2 * np.pi * 40* down_points) + 20 * np.sin(2 * np.pi * 80 * down_points) + 40 * np.sin(2*np.pi*160 * down_points)

plt.subplot(2, 2, 4)
plt.plot(down_points, signal_after_downSampling)
plt.xlabel('Time')
plt.ylabel('amplitude')
plt.title('Composite Signal after Down Sampling')
plt.grid()

plt.tight_layout()
plt.show()