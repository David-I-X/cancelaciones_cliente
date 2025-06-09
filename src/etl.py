import requests
import pandas as pd
import os

def extraer_datos(url):
    print("📥 Extrayendo datos desde la API...")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)

def transformar_datos(df):
    print("🔧 Transformando datos...")
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def cargar_datos(df, ruta_salida="data/datos_telecomx.csv"):
    print(f"💾 Guardando datos en {ruta_salida}")
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    df.to_csv(ruta_salida, index=False)

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json"
    
    df = extraer_datos(url)
    df = transformar_datos(df)
    cargar_datos(df)
    print("✅ Proceso ETL finalizado.")
