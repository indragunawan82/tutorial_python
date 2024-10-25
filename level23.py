# Contoh Unsupervised Learning: K-Means Clustering
# Contoh Kode: K-Means Clustering Kita akan mengelompokkan data pelanggan berdasarkan dua fitur (misalnya: jumlah pembelian dan total belanja).

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Data pelanggan (jumlah pembelian, total belanja)
data = np.array([
    [5, 200], [10, 400], [15, 800],
    [25, 500], [30, 700], [35, 1000]
])

# Membuat model K-Means
model = KMeans(n_clusters=2)
model.fit(data)

# Mendapatkan hasil clustering
labels = model.labels_

# Visualisasi hasil
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.title("K-Means Clustering")
plt.show()
