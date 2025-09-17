# SportsShoesBrand

-Temática: Marcas de zapatos deportivas 

Flujo ETL

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

    Ramas 
    # Descripción de ramas 

    - **main** → rama estable, solo código listo para producción. -> git config --get branch.main.description
    - **develop** → rama de integración, aquí se juntan nuevas features. -> git config --get branch.develop.description
    - **feature/etl** → desarrollo del pipeline ETL con Pandas y SQLite. -> git config --get branch.feature/etl.description

