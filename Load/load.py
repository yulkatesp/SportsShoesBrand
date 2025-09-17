import sqlite3
from Config.config import DB_PATH, OUTPUT_FILE, TABLE_NAME

def load_data(df):
    """Guarda los datos limpios en CSV y SQLite"""
    if df is None:
        return

    # Guardar en un nuevo CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"📂 Datos guardados en {OUTPUT_FILE}")

    # Guardar en SQLite
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()
    print(f"💾 Datos cargados en la base de datos {DB_PATH}")
