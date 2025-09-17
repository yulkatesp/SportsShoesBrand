import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(df):
    """Genera algunas gráficas básicas con Seaborn"""
    if df is None or df.empty:
        print("⚠️ No hay datos para graficar.")
        return

    # Ajustar estilo
    sns.set(style="whitegrid")

    # 1. Conteo de marcas por sitio (si existe columna 'sitio')
    if "sitio" in df.columns:
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x="sitio", order=df["sitio"].value_counts().index)
        plt.xticks(rotation=45)
        plt.title("Número de marcas por sitio")
        plt.tight_layout()
        plt.show()

    # 2. Distribución de seguidores de Twitter (si existe columna 'seguidores de twitter')
    if "seguidores de twitter" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(df["seguidores de twitter"], bins=20, kde=True)
        plt.title("Distribución de seguidores en Twitter")
        plt.xlabel("Seguidores de Twitter")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.show()

    # 3. Relación entre seguidores y tuits (si existen ambas columnas)
    if "seguidores de twitter" in df.columns and "tuits de twitter" in df.columns:
        plt.figure(figsize=(7, 5))
        sns.scatterplot(
            data=df,
            x="seguidores de twitter",
            y="tuits de twitter",
            hue="sitio" if "sitio" in df.columns else None,
            alpha=0.7
        )
        plt.title("Relación entre seguidores y tuits")
        plt.tight_layout()
        plt.show()

        plt.tight_layout()
        plt.savefig("plots/marcas_por_sitio.png")   # guarda la figura
        plt.close()  # cierra la figura para no saturar memoria

