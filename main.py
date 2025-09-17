from Extract.extract import extract_data
from Transform.transform import transform_data
from Load.load import load_data
from Visualize.graficas import plot_data

def main():
    # 1. Extraer
    df = extract_data()

    # 2. Transformar
    df_clean = transform_data(df)

    # Mostrar un preview
    if df_clean is not None:
        print("\n👀 Vista previa de los datos limpios:")
        print(df_clean.head())

        
        

        # 4. Cargar
        load_data(df_clean)

        
    else:
        print("❌ No se pudo transformar el DataFrame.")

    # 3. Visualización (usar df_clean, no df)
    print("\n📊 Generando visualizaciones...")
    #plot_data(df_clean)

if __name__ == "__main__":
    main()
