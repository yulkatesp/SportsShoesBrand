# SportsShoesBrand


-Temática: Marcas de zapatos deportivas 

# Estructura

    ├── Config/ # Configuración general del proyecto
    │ ├── config.py
    │ └── init.py
    │
    ├── Extract/ # Extracción de datos
    │ ├── extract.py
    │ └── init.py
    │
    ├── Load/ # Carga de datos a la base de datos
    │ └── load.py
    │
    ├── Plots/ # Carpeta destinada a guardar gráficas generadas
    │
    ├── Transform/ # Transformación y limpieza de datos
    │ ├── transform.py
    │ └── init.py
    │
    ├── Visualize/ # Scripts para visualización de datos
    │ ├── graficas.py
    │ └── init.py
    │
    ├── brands.csv # Dataset original
    ├── brands_clean.csv # Dataset limpio después de la transformación
    ├── brands_clean.db # Base de datos SQLite con la información procesada
    ├── main.py # Script principal para ejecutar el pipeline ETL
    └── README.md # Documentación del proyecto



# Flujo ETL

    Extract

        Lee el archivo brands.csv con Pandas.

    Transform

        Elimina duplicados.

        Elimina filas vacías.

        Rellena valores nulos con "Desconocido" (texto) o 0 (numéricos).

        Limpia los nombres de columnas (quita espacios).

    Load

        Guarda el DataFrame limpio en:

        brands_clean.csv

        Base de datos SQLite: brands_clean.db, tabla brands.

    Output

        Muestra en consola una vista previa de los datos limpios (head).


    Tecnologías usadas

        Python 3

        Pandas

        SQLite3

    
 # Descripción de ramas 

    - **main** → rama estable, solo código listo para producción. -> git config --get branch.main.description
    - **develop** → rama de integración, aquí se juntan nuevas features. -> git config --get branch.develop.description
    - **feature/etl** → desarrollo del pipeline ETL con Pandas y SQLite. -> git config --get branch.feature/etl.description



