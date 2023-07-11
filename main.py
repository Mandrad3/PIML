import pandas as pd
from fastapi import FastAPI
import  uvicorn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


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
        duracion = df_pelicula.iloc[0]['runtime']
        año = df_pelicula.iloc[0]['release_year']
        
        return f"Película: {pelicula}. Duración: {duracion}. Año: {año}"
    else:
        return f"No se encontró la película: {pelicula}"

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    df = pd.read_csv('collection.csv')  # Leer el archivo CSV
    
    # Filtrar por la franquicia especificada
    df_franquicia = df[df['name_collection'] == franquicia]
    
    # Obtener la cantidad de películas y la ganancia total
    cantidad_peliculas = len(df_franquicia)
    ganancia_total = df_franquicia['revenue'].sum()
    
    # Calcular el promedio de ganancia por película
    ganancia_promedio = ganancia_total / cantidad_peliculas
    
    return {
        "franquicia": franquicia,
        "peliculas": cantidad_peliculas,
        "ganancia_total": ganancia_total,
        "ganancia_promedio": ganancia_promedio
    }

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    # Leer el archivo CSV con pandas
    df = pd.read_csv('country.csv')
    
    # Filtrar el DataFrame por el país consultado
    df_pais = df[df['production_countries'] == pais]
    
    # Obtener la cantidad de películas en el país
    cantidad = len(df_pais)
    
    return f"Se produjeron {cantidad} películas en el país {pais}"

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

df = pd.read_csv('datos.csv')

# Crea una muestra aleatoria con 5000 filas del dataset
muestra = df.head(5000)

# Crea la matriz de características TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(muestra['overview'].fillna(''))

# Calcula la similitud coseno entre todas las descripciones
cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

# Función que calcula la similitud entre dos conjuntos de géneros cinematográficos
def calcular_similitud_generos(generos_referencia, generos):
    if pd.isnull(generos_referencia) or pd.isnull(generos):
        return 0.0

    generos_referencia = set(generos_referencia.split('|'))
    generos = set(generos.split('|'))
    intersection = len(generos_referencia.intersection(generos))
    union = len(generos_referencia.union(generos))
    return intersection / union

# Crea la función de recomendación
@app.get("/recomendacion")
def recomendacion(titulo: str):
    # Busca el id de la pelicula en la muestra
    idx = muestra[muestra['title'] == titulo].index[0]
    sim_cosine = cosine_similarity[idx]

    # Calcula la similitud de géneros para la película de referencia
    generos_referencia = muestra.loc[idx, 'genres']
    sim_generos = muestra['genres'].apply(lambda x: calcular_similitud_generos(generos_referencia, x))

    # Combina la similitud coseno y la similitud de géneros
    sim_total = sim_cosine + sim_generos

    # Obtiene los índices de las películas similares
    similar_indices = sim_total.argsort()[::-1][1:6]

    # Obtiene los títulos de las películas similares
    similar_movies = muestra['title'].iloc[similar_indices].tolist()

    return similar_movies

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=10000)