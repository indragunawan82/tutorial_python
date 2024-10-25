#  Decision Tree dengan Scikit-Learn
#  Decision Tree Kita akan menggunakan Decision Tree Classifier untuk memprediksi apakah seseorang akan membeli produk berdasarkan usia dan pendapatan.

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Data (usia dan pendapatan) dan label (0: Tidak Beli, 1: Beli)
X = [[25, 50000], [30, 60000], [35, 65000], [40, 70000], [45, 80000]]
y = [0, 0, 1, 1, 1]  # Label target

# Split data menjadi train dan test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Membuat dan melatih model Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Memprediksi data test
y_pred = model.predict(X_test)

# Evaluasi model
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
