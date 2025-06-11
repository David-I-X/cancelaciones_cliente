import requests
import pandas as pd
import os

def extraer_datos(url):
    print(" Extrayendo datos desde la API...")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)

def transformar_datos(df):
    print(" Transformando datos...")

    # Aplanar columnas anidadas
    columnas_anidadas = ['customer', 'phone', 'internet', 'account']

    for col in columnas_anidadas:
        anidada = pd.json_normalize(df[col])
        anidada.columns = [f"{col}_{subcol}".lower() for subcol in anidada.columns]
        df = pd.concat([df.drop(columns=[col]), anidada], axis=1)

    # Normalizar nombres de columnas
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    
    return df

def cargar_datos(df, ruta_salida="data/datos_telecomx.csv"):
    # Obtener el directorio de la ruta de salida
    directorio = os.path.dirname(ruta_salida)
    
    # Crear el directorio si no existe
    if not os.path.exists(directorio):
        print(f" Creando directorio: {directorio}")
        os.makedirs(directorio)
    
    # Guardar los datos
    print(f" Guardando datos en {ruta_salida}")
    df.to_csv(ruta_salida, index=False)

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json"
    
    df = extraer_datos(url)
    df = transformar_datos(df)
    cargar_datos(df)
    print("✅ Proceso ETL finalizado.")
