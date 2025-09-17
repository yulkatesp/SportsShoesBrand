import pandas as pd
from Config.config import INPUT_FILE

def extract_data():
    """Lee el archivo CSV y devuelve un DataFrame"""
    try:
        df = pd.read_csv(INPUT_FILE)
        print("✅ Datos extraídos correctamente.")
        return df
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None

