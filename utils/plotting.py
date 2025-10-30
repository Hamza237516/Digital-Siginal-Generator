import matplotlib.pyplot as plt
import numpy as np

def plot_signal(data, signal, title="Digital Signal"):
    t = np.arange(0, len(signal))
    plt.step(t, signal, where='post')
    plt.ylim(-2, 2)
    plt.xlabel('Bit Index')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.grid(True)
    plt.show()

