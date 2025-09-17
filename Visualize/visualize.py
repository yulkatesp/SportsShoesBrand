import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Cargar datos
df = pd.read_csv("brands.csv")

# Gráfico de barras — Comparación seguidores de Twitter y Facebook
plt.figure(figsize=(12,6))
sns.barplot(x="name", y="twitter", data=df, color="skyblue", label="Twitter")
sns.barplot(x="name", y="facebook", data=df, color="salmon", alpha=0.7, label="Facebook")
plt.title("Seguidores en Twitter vs Facebook por Marca", fontsize=14, weight="bold")
plt.xticks(rotation=90)
plt.ylabel("Número de Seguidores")
plt.legend()
plt.tight_layout()
plt.show()

#Gráfico de dispersión — Relación entre seguidores y seguidos en Twitter

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="twitter_following", y="twitter_followers", hue="name", s=100)
plt.title("Relación: Seguidos vs Seguidores en Twitter", fontsize=14, weight="bold")
plt.xlabel("Siguiendo en Twitter")
plt.ylabel("Seguidores en Twitter")
plt.legend(bbox_to_anchor=(1.05,1), loc="upper left")
plt.tight_layout()
plt.show()

#Histograma — Distribución de seguidores en Twitter

plt.figure(figsize=(10,6))
sns.histplot(df["twitter_followers"], bins=15, kde=True, color="purple")
plt.title("Distribución de Seguidores en Twitter", fontsize=14, weight="bold")
plt.xlabel("Cantidad de Seguidores")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()
