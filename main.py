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