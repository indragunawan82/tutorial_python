# import tensorflow as tf
# print(tf.__version__)


import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Dataset (Jam Belajar dan Status Lulus)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # 0: Tidak Lulus, 1: Lulus

# 2. Membuat Model Neural Network Sederhana
model = Sequential([
    Dense(1, input_shape=(1,), activation='sigmoid')  # Lapisan Tunggal
])

# Compile model dengan optimizer dan fungsi loss
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3. Melatih Model
print("Mulai Training...")
model.fit(X, y, epochs=50)

# 4. Memprediksi Data Baru
prediksi = model.predict([[5]])  # Prediksi apakah siswa dengan 5 jam belajar akan lulus
print(f"Prediksi untuk siswa dengan 5 jam belajar: {prediksi[0][0]:.2f}")
