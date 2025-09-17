import seaborn as sns
import matplotlib.pyplot as plt
import os


def plot_data(df):
    """Genera gráficas básicas con Seaborn y las guarda en /Plots"""

    if df is None or df.empty:
        print("❌ No hay datos para graficar.")
        return

    # Crear carpeta de salida si no existe
    os.makedirs("Plots", exist_ok=True)

    sns.set(style="whitegrid")

    # 1. Conteo de registros por columna 'sitio'
    if "sitio" in df.columns:
        plt.figure(figsize=(8,5))
        sns.countplot(data=df, x="sitio", order=df["sitio"].value_counts().index[:10])
        plt.title("Top 10 Sitios más frecuentes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("Plots/top_sitios.png")  # guardar primero
        plt.show()

    # 2. Distribución de seguidores de Twitter
    if "seguidores de twitter" in df.columns:
        plt.figure(figsize=(8,5))
        sns.histplot(df["seguidores de twitter"], bins=30, kde=True)
        plt.title("Distribución de Seguidores en Twitter")
        plt.xlabel("Seguidores")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.savefig("Plots/distribucion_seguidores.png")
        plt.show()

    # 3. Relación entre tuits y seguidores
    if "seguidores de twitter" in df.columns and "tuits de twitter" in df.columns:
        plt.figure(figsize=(8,5))
        sns.scatterplot(data=df, x="tuits de twitter", y="seguidores de twitter", alpha=0.6)
        plt.title("Relación entre Tuits y Seguidores en Twitter")
        plt.xlabel("Número de Tuits")
        plt.ylabel("Seguidores")
        plt.tight_layout()
        plt.savefig("Plots/relacion_tuits_seguidores.png")
        plt.show()

    print("✅ Gráficas guardadas en carpeta: Plots/")
