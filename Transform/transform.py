
def transform_data(df):
    """Limpieza básica de los datos"""
    if df is None:
        return None

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Eliminar filas completamente vacías
    df = df.dropna(how="all")

    # Reemplazar valores nulos con 'Desconocido' en texto y 0 en números
    df = df.fillna({
        col: "Desconocido" if df[col].dtype == "object" else 0
        for col in df.columns
    })

    # Quitar espacios en los nombres de columnas
    df.columns = [col.strip() for col in df.columns]

    print("✅ Datos transformados (limpios).")
    return df
