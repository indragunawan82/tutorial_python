import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title('Contoh Grafik')
plt.show()



# Seaborn: Untuk visualisasi data statistik yang lebih kompleks.
import seaborn as sns
sns.set(style="darkgrid")

tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()