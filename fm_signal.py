import numpy as np
import matplotlib.pyplot as plt

# Sampling rate and duration
fs = 1e6  # 1 MHz sampling rate
duration = 0.01  # 10 ms duration
t = np.arange(0, duration, 1/fs)

# Message signal (e.g., an audio signal)
fm = 1e3  # 1 kHz frequency of the message signal
message = np.sin(2 * np.pi * fm * t)

# Carrier signal
fc = 100e3  # 100 kHz carrier frequency
carrier = np.cos(2 * np.pi * fc * t)

# FM modulation
modulation_index = 2.0
fm_signal = np.cos(2 * np.pi * fc * t + modulation_index * np.cumsum(message) / fs)

# Visualizing the signals
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t[:1000], message[:1000])
plt.title('Message Signal')
plt.subplot(3, 1, 2)
plt.plot(t[:1000], carrier[:1000])
plt.title('Carrier Signal')
plt.subplot(3, 1, 3)
plt.plot(t[:1000], fm_signal[:1000])
plt.title('FM Modulated Signal')
plt.tight_layout()
plt.show()
