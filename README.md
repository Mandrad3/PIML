# PIML
# API de Películas

Esta API permite consultar información relacionada con películas, como idioma, duración, franquicias, países de producción, productoras exitosas, directores y recomendaciones.

Esta API permite consultar información relacionada con películas, como idioma, duración, franquicias, países de producción, productoras exitosas, directores y recomendaciones.

La API está actualmente desplegada y disponible en [https://api-peliculas-piml.onrender.com](https://api-peliculas-piml.onrender.com).
 
 en caso de que eventualmente no este despleagada puedes instalarla siguiendo estos pasos.

## Instalación

1. Clona el repositorio en tu máquina local.
2. Instala las dependencias ejecutando el siguiente comando:
pip install -r requirements.txt

Ejecuta la API con el siguiente comando:
uvicorn main:app --reload
La API estará disponible en http://localhost:10000.

Endpoints
Obtener mensaje de bienvenida

GET /
Devuelve un mensaje de bienvenida.

Obtener cantidad de películas por idioma

GET /peliculas_idioma/{idioma}
Retorna la cantidad de películas estrenadas en el idioma especificado.

Obtener duración y año de una película

GET /peliculas_duracion/{pelicula}
Devuelve la duración y el año de estreno de una película.

Obtener información de una franquicia

GET /franquicia/{franquicia}
Retorna la cantidad de películas, la ganancia total y la ganancia promedio de una franquicia.

Obtener cantidad de películas por país

GET /peliculas_pais/{pais}
Devuelve la cantidad de películas producidas en un país específico.

Obtener información de una productora exitosa

GET /productoras_exitosas/{productora}
Retorna la ganancia total y la cantidad de películas realizadas por una productora.

Obtener éxito de un director y lista de películas

GET /get_director/{nombre_director}
Devuelve el éxito del director medido por el retorno total y una lista de películas dirigidas por él, con información como título, fecha de lanzamiento, retorno, costo y ganancia.

Recomendación de películas similares

GET /recomendacion?titulo={titulo}
Obtiene una lista de películas similares a la especificada en el parámetro titulo.

Dataset
El código utiliza varios archivos CSV como fuente de datos. Asegúrate de tener los siguientes archivos en la misma ubicación que el archivo main.py:

idioma.csv: contiene información sobre las películas y su idioma.
duracion.csv: contiene información sobre las películas y su duración.
collection.csv: contiene información sobre las franquicias y sus películas.
country.csv: contiene información sobre las películas y los países de producción.
production.csv: contiene información sobre las productoras y sus películas.
cast.csv: contiene información sobre el reparto, incluyendo directores.
Contribuciones

## Resumen del Trabajo de ETL

En este proyecto, se realizó un proceso de Extracción, Transformación y Carga (ETL) de datos utilizando la biblioteca Pandas de Python. El objetivo principal fue limpiar y transformar un conjunto de datos de películas para su posterior análisis.

### Extracción de datos

Se realizaron las siguientes operaciones de extracción:

- Lectura de los archivos CSV `movies_dataset.csv` y `credits.csv`.
- Corrección del formato de JSON en la columna "belongs_to_collection" de `movies_dataset.csv`.
- Extracción de datos de las columnas "belongs_to_collection", "production_companies", "genres", "production_countries", "cast" y "crew" de los archivos de datos.

### Transformación de datos

Se aplicaron varias transformaciones a los datos, incluyendo:

- Conversión de formatos de JSON a objetos Python utilizando las funciones `json.loads()` y `ast.literal_eval()`.
- Extracción de información específica de las columnas "belongs_to_collection", "production_companies", "genres", "production_countries", "cast" y "crew".
- Concatenación de datos en un solo DataFrame para facilitar su manejo posterior.

### Carga de datos

Se guardaron los datos transformados en archivos CSV para su uso posterior. Los archivos resultantes son:

- `idioma.csv`: Contiene los datos de las columnas "id" y "original_language".
- `duracion.csv`: Contiene los datos de las columnas "id", "title", "runtime" y "release_year".
- `collection.csv`: Contiene los datos de las columnas "id", "name_collection" y "revenue".
- `country.csv`: Contiene los datos de las columnas "id" y "production_countries".
- `production.csv`: Contiene los datos de las columnas "id", "production_companies" y "revenue".
- `cast.csv`: Contiene los datos de las columnas "id", "director", "actors", "return", "budget", "revenue", "title" y "release_date".
- `datos.csv`: Contiene la combinación de los datos de `movies_dataset.csv` y `credits.csv`.

Estos archivos pueden ser utilizados como fuente de datos para el análisis de películas.

## Resumen del Trabajo de Análisis Exploratorio de Datos (EDA)

En este proyecto de Análisis Exploratorio de Datos (EDA), se utilizó la biblioteca Pandas de Python para explorar y visualizar un conjunto de datos de películas.

### Extracción de datos

Se realizó la extracción de datos mediante la lectura de un archivo CSV llamado `datos.csv`. Se observó que algunas columnas presentaban advertencias de tipo de datos mixtos, lo cual se tuvo en cuenta durante el análisis.

### Análisis general de la información

Se realizó un análisis general de la información presente en el conjunto de datos. Se mostró la forma del DataFrame y se imprimieron las primeras filas para tener una visión general de la estructura de los datos. También se utilizó el método `info()` para obtener información detallada sobre las columnas y sus tipos de datos.

Se calcularon estadísticas descriptivas para las columnas numéricas, como presupuesto, ganancia, duración y más.

### Visualización de datos

Se utilizaron diferentes técnicas de visualización para explorar los datos de películas:

- Mapa de calor: Se creó un mapa de calor para visualizar la matriz de correlación entre las variables numéricas del conjunto de datos.
- Gráficos de dispersión: Se crearon gráficos de dispersión para analizar las relaciones entre variables, como el conteo de votos vs presupuesto, conteo de votos vs ganancia, año de estreno vs ganancia y voto promedio vs ganancia.
- Gráficos de barras: Se crearon gráficos de barras para mostrar la cantidad de películas por género.
- Nubes de palabras: Se generaron nubes de palabras para visualizar palabras clave en las columnas de descripción, géneros y directores.

### Conclusiones

Este proyecto de Análisis Exploratorio de Datos (EDA) proporcionó una visión general de los datos de películas, incluyendo información sobre presupuesto, ganancia, géneros, directores y más. La visualización de datos permitió identificar patrones y tendencias interesantes. Los resultados obtenidos pueden servir como punto de partida para análisis más profundos y toma de decisiones en la industria cinematográfica.
