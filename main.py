from fastapi import FastAPI
import pandas as pd
import uvicorn


app = FastAPI()

df1 = pd.read_csv("mes_estreno.csv")
df2 = pd.read_csv("dia_estreno.csv")

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
        
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=10000)