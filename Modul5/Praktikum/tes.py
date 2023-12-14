import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]

# Misalnya interval ukuran per 10 sentimeter
interval_size = 10

# TODO 1: Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def create_intervals(data, interval_size):
    min_val = min(data)
    max_val = max(data)
    intervals = np.arange(min_val, max_val + interval_size, interval_size)
    return intervals

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
def count_frequencies(data, intervals):
    frequencies = []
    for i in range(len(intervals) - 1):
        freq = sum(1 for x in data if intervals[i] <= x <= intervals[i+1])
        frequencies.append(freq)
    return frequencies

# TODO 3: Visualisasi data dalam bentuk histogram
def plot_histogram(data, frequencies, intervals):
    plt.hist(data, bins=intervals, density=True, alpha=0.6, edgecolor='black', bottom=0)
    plt.xlabel('Tinggi Badan (cm)')
    plt.ylabel('Frekuensi')
    plt.title('Distribusi Tinggi Badan Menggunakan Histogram')

# TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
def plot_pdf(data, intervals):
    mean = np.mean(data)
    std_dev = np.std(data)
    x = np.linspace(min(data), max(data), 100)
    y = norm.pdf(x, mean, std_dev)
    plt.plot(x, y, color='red', linewidth=2, label='PDF')
    plt.xlabel('Tinggi Badan (cm)')
    plt.ylabel('PDF')
    plt.title('Distribusi Tinggi Badan Menggunakan PDF')
    plt.legend()


intervals = create_intervals(tinggi_badan, interval_size)
frequencies = count_frequencies(tinggi_badan, intervals)
plot_histogram(tinggi_badan, frequencies, intervals)
plot_pdf(tinggi_badan, intervals)

plt.show()
