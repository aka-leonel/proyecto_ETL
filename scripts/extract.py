import os
import requests
import logging
from datetime import datetime
from pathlib import Path
from config import SOURCES

# Configuración de logs básica para este módulo 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def descargar_archivo(categoria, url):
    """
    Descarga un CSV desde una URL y lo guarda en la estructura de carpetas requerida.
    """
    try:
       # Diccionario manual para asegurar el español
        meses_es = {
            1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
            5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
        }
        
        # 1. Obtener fecha actual
        hoy = datetime.now()
        nombre_mes = meses_es[hoy.month]  # <--- Cambio aquí
        anio_mes = f"{hoy.year}-{nombre_mes}"
        nombre_archivo = f"{categoria}-{hoy.strftime('%d-%m-%Y')}.csv"

        # 2. Crear la ruta de destino 
        # Ruta: categoria/año-mes/
        ruta_carpeta = Path(f"data/{categoria}/{anio_mes}")
        ruta_carpeta.mkdir(parents=True, exist_ok=True)
        
        ruta_final = ruta_carpeta / nombre_archivo

        # 3. Descarga con requests 
        logging.info(f"Descargando {categoria} desde {url}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Lanza error si la descarga falla 

        # 4. Guardar archivo (Si existe, se reemplaza) [cite: 20]
        with open(ruta_final, 'wb') as f:
            f.write(response.content)
        
        logging.info(f"Archivo guardado en: {ruta_final}")
        return ruta_final

    except requests.exceptions.RequestException as e:
        logging.error(f"Error al descargar {categoria}: {e}")
        return None

def ejecutar_extraccion():
    """
    Orquestador de la fase de extracción.
    """
    rutas_descargadas = {}
    for categoria, url in SOURCES.items():
        ruta = descargar_archivo(categoria, url)
        if ruta:
            rutas_descargadas[categoria] = ruta
    return rutas_descargadas

if __name__ == "__main__":
    ejecutar_extraccion()