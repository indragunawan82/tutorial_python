import numpy as np
from sklearn.linear_model import LinearRegression

# Data (luas dalam m² dan harga dalam juta rupiah)
luas = np.array([[30], [50], [70], [90], [110]])
harga = np.array([300, 500, 700, 900, 1100])

# Membuat dan melatih model
model = LinearRegression()
model.fit(luas, harga)

# Memprediksi harga untuk rumah dengan luas 60 m²
prediksi = model.predict([[60]])
print(f"Harga rumah untuk luas 60 m²: {prediksi[0]} juta")
