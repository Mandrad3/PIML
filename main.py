from fastapi import FastAPI
import pandas as pd
import uvicorn


app = FastAPI()

@app.get('/')
def root():
    return {"message": "¡Bienvenido a mi API!"}

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    # Convertir el idioma a minúsculas para realizar la comparación
    idioma = idioma.lower()

    # Leer el archivo CSV con pandas y filtrar por el idioma consultado
    df = pd.read_csv('idioma.csv')
    df_idioma = df[df['original_language'].str.lower() == idioma]

    # Obtener la cantidad de películas en el idioma
    cantidad = len(df_idioma)

    return f"{cantidad} cantidad de películas fueron estrenadas en idioma {idioma}"

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    # Leer el archivo CSV con pandas y filtrar por la película consultada
    df = pd.read_csv('duracion.csv')
    df_pelicula = df[df['title'] == pelicula]

    # Verificar si se encontró una coincidencia
    if not df_pelicula.empty:
        # Obtener los datos de la película
        duracion = df_pelicula.iloc[0]['duracion']
        año = df_pelicula.iloc[0]['release_year']
        
        return f"Película: {pelicula}. Duración: {duracion}. Año: {año}"
    else:
        return f"No se encontró la película: {pelicula}"

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    # Leer el archivo CSV con pandas y filtrar por la franquicia consultada
    df = pd.read_csv('duracion.csv')
    df_franquicia = df[df['name_collection'] == franquicia]

    # Verificar si se encontraron películas de la franquicia
    if not df_franquicia.empty:
        # Obtener la cantidad de películas de la franquicia
        cantidad_peliculas = len(df_franquicia)

        # Calcular la ganancia total y promedio de la franquicia
        ganancia_total = df_franquicia['revenue'].sum()
        ganancia_promedio = df_franquicia['revenue'].mean()

        return f"La franquicia {franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"
    else:
        return f"No se encontraron películas de la franquicia: {franquicia}"

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    # Leer el archivo CSV de países con pandas
    df_paises = pd.read_csv('country.csv')

    # Filtrar el DataFrame por el país consultado
    df_pais = df_paises[df_paises['id'] == pais]

    # Obtener el nombre completo del país
    nombre_pais = df_pais.iloc[0]['production_countries']

    # Leer el archivo CSV de idiomas con pandas
    df_idiomas = pd.read_csv('idioma.csv')

    # Filtrar el DataFrame por el país consultado
    df_idioma_pais = df_idiomas[df_idiomas['id'] == pais]

    # Obtener la cantidad de películas producidas en el país
    cantidad_peliculas = len(df_idioma_pais)

    return f"Se produjeron {cantidad_peliculas} películas en el país {nombre_pais}"

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora: str):
    # Leer el archivo CSV de producción con pandas
    df_production = pd.read_csv('production.csv')

    # Filtrar el DataFrame por la productora consultada
    df_productora = df_production[df_production['production_companies'] == productora]

    # Calcular el total de ingresos
    revenue_total = df_productora['revenue'].sum()

    # Obtener la cantidad de películas realizadas
    cantidad_peliculas = len(df_productora)

    return f"La productora {productora} ha tenido un revenue de {revenue_total} y ha realizado {cantidad_peliculas} películas"
@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    # Leer el archivo CSV de reparto con pandas
    df_cast = pd.read_csv('cast.csv')

    # Filtrar el DataFrame por el nombre del director
    df_director = df_cast[df_cast['director'] == nombre_director]

    # Calcular el éxito del director (retorno total)
    exito_director = df_director['return'].sum()

    # Obtener la información de cada película dirigida por el director
    peliculas = []
    for index, row in df_director.iterrows():
        titulo = row['title']
        fecha_lanzamiento = row['release_date']
        retorno = row['return']
        costo = row['budget']
        ganancia = row['revenue']
        peliculas.append({
            'titulo': titulo,
            'fecha_lanzamiento': fecha_lanzamiento,
            'retorno': retorno,
            'costo': costo,
            'ganancia': ganancia
        })

    return {
        'exito_director': exito_director,
        'peliculas': peliculas
    }
        
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=10000)