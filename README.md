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
