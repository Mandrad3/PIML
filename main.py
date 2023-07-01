from fastapi import FastAPI
import pandas as pd
import uvicorn


app = FastAPI()

@app.get('/')
def root():
    return {"message": "¡Bienvenido a mi API!"}

# Función para obtener la cantidad de filmaciones en un mes específico
@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    # Convertir el mes a minúsculas para realizar la comparación
    mes = mes.lower()

    # Leer el archivo CSV con pandas y filtrar por el mes consultado
    df = pd.read_csv('mes_estreno.csv')
    df_mes = df[df['release_month'].str.lower() == mes]

    # Obtener la cantidad de películas en el mes
    cantidad = len(df_mes)

    return f"{cantidad} cantidad de películas fueron estrenadas en el mes de {mes}"

df_dia_estreno = pd.read_csv("dia_estreno.csv")

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str):
    # Convertir el día a minúsculas para realizar la comparación
    dia = dia.lower()
    
    # Filtrar el DataFrame por el día consultado
    df_dia = df_dia_estreno[df_dia_estreno['release_day'] == dia]
    
    # Obtener la cantidad de películas en el día
    cantidad = len(df_dia)
    
    return f"{cantidad} cantidad de películas fueron estrenadas en los días {dia}"

        
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=10000)