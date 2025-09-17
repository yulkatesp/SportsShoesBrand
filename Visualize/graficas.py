import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_data(csv_path="brand_clean.csv", output_dir="Plots"):
    """
    Genera gráficas básicas con Seaborn y las guarda en /Visualize/Plots
    """

    # Cargar datos desde CSV limpio
    if not os.path.exists(csv_path):
        print(f"❌ No se encontró el archivo {csv_path}")
        return

    df = pd.read_csv(csv_path)

    if df.empty:
        print("❌ El DataFrame está vacío, no se generarán gráficas.")
        return

    # Crear carpeta de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Estilo pastel
    sns.set_palette("pastel")
    plt.style.use("seaborn-v0_8-whitegrid")

    # === 1. Conteo de registros por sitio (Top 10) ===
    if "sitio" in df.columns:
        top_sites = df["sitio"].value_counts().head(10)

        plt.figure(figsize=(10, 6))
        sns.barplot(
            x=top_sites.values,
            y=top_sites.index,
            palette="pastel"
        )
        plt.title("Top 10 Sitios más frecuentes", fontsize=14, weight="bold")
        plt.xlabel("Cantidad de registros")
        plt.ylabel("Sitio")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "top_sitios.png"))
        plt.close()

    # === 2. Distribución de seguidores de Twitter ===
    if "seguidores de twitter" in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df["seguidores de twitter"], bins=30, kde=True, color="skyblue")
        plt.title("Distribución de Seguidores en Twitter", fontsize=14, weight="bold")
        plt.xlabel("Número de Seguidores")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "distribucion_seguidores.png"))
        plt.close()

    # === 3. Relación entre tuits y seguidores ===
    if "seguidores de twitter" in df.columns and "tuits de twitter" in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            data=df,
            x="tuits de twitter",
            y="seguidores de twitter",
            alpha=0.6,
            color="coral"
        )
        plt.title("Relación entre Tuits y Seguidores en Twitter", fontsize=14, weight="bold")
        plt.xlabel("Número de Tuits")
        plt.ylabel("Número de Seguidores")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "relacion_tuits_seguidores.png"))
        plt.close()

    print(f"✅ Gráficas pastel guardadas en {output_dir}/")