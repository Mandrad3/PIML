from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

df1 = pd.read_csv("mes_estreno.csv")
df2 = pd.read_csv("dia_estreno.csv")

# Función para obtener la cantidad de filmaciones en un mes específico
@app.get('/cantidad_filmaciones_mes')
def cantidad_filmaciones_mes(mes: str):
    # Convertir el mes a minúsculas para realizar la comparación
    mes = mes.lower()
    
    # Filtrar el DataFrame por el mes consultado
    df_mes = df1[df1['release_month'] == mes]
    
    # Obtener la cantidad de películas en el mes
    cantidad = len(df_mes)

    return {"cantidad": cantidad}

@app.get('/cantidad_filmaciones_dia')
def cantidad_filmaciones_dia(dia: str):
    # Convertir el día a minúsculas para realizar la comparación
    dia = dia.lower()
    
    # Filtrar el DataFrame por el día consultado
    df_dia = df2[df2['release_day'] == dia]
    
    # Obtener la cantidad de películas en el día
    cantidad = len(df_dia)
    
    return {"cantidad": cantidad}

# Función de ejemplo para buscar un título en el archivo CSV y obtener los datos correspondientes
def buscar_titulo(titulo):
    with open('popularity.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['title'] == titulo:
                return row
    return None

# Endpoint para obtener el score de una filmación por título
@app.get('/score_titulo/{titulo}')
def score_titulo(titulo: str):
    # Lógica para buscar el título en el archivo CSV y obtener el score y el año de estreno
    resultado = buscar_titulo(titulo)
    if resultado:
        return f'La película {resultado["title"]} fue estrenada en el año {resultado["release_year"]} con un score/popularidad de {resultado["vote_average"]}'
    else:
        return f'No se encontró la película con título {titulo}'

# Endpoint para obtener la cantidad de votos y el valor promedio de votaciones por título de filmación
@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo: str):
    # Lógica para buscar el título en el archivo CSV y obtener la cantidad de votos y el valor promedio
    resultado = buscar_titulo(titulo)
    if resultado:
        votos = resultado["vote_count"]
        promedio = resultado["vote_average"]
        if int(votos) >= 2000:
            return f'La película {resultado["title"]} fue estrenada en el año {resultado["release_year"]}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {promedio}.'
        else:
            return f'La película {resultado["title"]} fue estrenada en el año {resultado["release_year"]}, pero no cumple con la condición de tener al menos 2000 valoraciones.'
    else:
        return f'No se encontró la película con título {titulo}'
    
    # Endpoint para obtener información de un actor por su nombre
@app.get('/get_actor/{nombre}')
def get_actor(nombre: str):
    # Lógica para buscar el nombre del actor en el archivo CSV y obtener información relacionada
    resultado = buscar_actor(nombre)
    if resultado:
        cantidad_peliculas = resultado["cantidad_peliculas"]
        retorno_total = resultado["retorno_total"]
        promedio_retorno = resultado["promedio_retorno"]
        return f'El actor {nombre} ha participado en {cantidad_peliculas} filmaciones. Ha conseguido un retorno total de {retorno_total} con un promedio de {promedio_retorno} por filmación.'
    else:
        return f'No se encontró al actor con nombre {nombre}'

# Función de ejemplo para buscar un actor en el archivo CSV y obtener información relacionada
def buscar_actor(nombre):
    with open('cast.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        cantidad_peliculas = 0
        retorno_total = 0
        contador = 0
        for row in reader:
            actors = row['actors'].split(',')
            if nombre in actors:
                if row['Director'] == '':
                    cantidad_peliculas += 1
                    retorno_total += float(row['return'])
                    contador += 1
        if contador > 0:
            promedio_retorno = retorno_total / contador
            return {"cantidad_peliculas": cantidad_peliculas, "retorno_total": retorno_total, "promedio_retorno": promedio_retorno}
        else:
            return None
        
        # Endpoint para obtener información de un director por su nombre
@app.get('/get_director/{nombre}')
def get_director(nombre: str):
    # Lógica para buscar el nombre del director en el archivo CSV y obtener información relacionada
    resultado = buscar_director(nombre)
    if resultado:
        peliculas = resultado["peliculas"]
        return f'El director {nombre} ha tenido éxito con las siguientes películas:\n\n{peliculas}'
    else:
        return f'No se encontró al director con nombre {nombre}'

# Función de ejemplo para buscar un director en el archivo CSV y obtener información relacionada
def buscar_director(nombre):
    with open('cast.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        peliculas = []
        for row in reader:
            if row['director'] == nombre:
                pelicula = {
                    "titulo": row['title'],
                    "fecha_lanzamiento": row['release_date'],
                    "retorno_individual": row['return'],
                    "costo": row['budget'],
                    "ganancia": row['revenue']
                }
                peliculas.append(pelicula)
        if peliculas:
            return {"peliculas": peliculas}
        else:
            return None
        
if __name__ == '__main__':
uvicorn.run(app, host='0.0.0.0', port=10000)