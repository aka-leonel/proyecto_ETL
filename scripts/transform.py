import pandas as pd
import logging
from datetime import datetime
from config import SOURCES, COLUMN_MAPPING, FINAL_COLUMNS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def normalizar_datos(df, categoria):
    """
    Filtra, renombra y normaliza las columnas de un DataFrame.
    """
    # 1. Renombrar columnas según el mapeo en config.py
    df = df.rename(columns=COLUMN_MAPPING)
    
    # 2. Asegurar que existan todas las columnas requeridas (llenar con nulos si faltan) 
    for col in FINAL_COLUMNS:
        if col not in df.columns:
            df[col] = None
            
    # 3. Seleccionar solo las columnas finales requeridas 
    df = df[FINAL_COLUMNS].copy()
    
    # 4. Agregar columna de categoria y fecha de carga 
    df['categoria'] = categoria
    df['fecha_carga'] = datetime.now().date()
    
    return df

def generar_tabla_totales(df_unificado):
    """
    Crea la tabla de agregados con información clara por provincia y categoría.
    """
    # --- 1. Totales por categoría (Nacional) ---
    totales_cat = df_unificado.groupby('categoria').size().reset_index(name='cantidad')
    totales_cat['descripcion'] = 'Total nacional por categoría'
    totales_cat['provincia'] = 'Todas'  # Para que no quede nulo y sea claro
    
    # --- 2. Totales por provincia y categoría ---
    totales_prov_cat = df_unificado.groupby(['provincia', 'categoria']).size().reset_index(name='cantidad')
    totales_prov_cat['descripcion'] = 'Total provincial por categoría'
    # Aquí la columna 'provincia' ya existe gracias al groupby
    
    # --- 3. Combinar ---
    resumen = pd.concat([totales_cat, totales_prov_cat], ignore_index=True)
    resumen['fecha_carga'] = datetime.now().date()
    
    # Reordenar columnas para que la lectura sea lógica: Descripcion | Provincia | Categoria | Cantidad
    column_order = ['descripcion', 'provincia', 'categoria', 'cantidad', 'fecha_carga']
    return resumen[column_order]

def ejecutar_transformacion(rutas_archivos):
    """
    Orquestador de la fase de transformación.
    """
    dfs_procesados = []
    
    for categoria, ruta in rutas_archivos.items():
        logging.info(f"Procesando {categoria} desde {ruta}...")
        df_raw = pd.read_csv(ruta)
        
        df_norm = normalizar_datos(df_raw, categoria)
        dfs_procesados.append(df_norm)
    
    # Unificar todos los DataFrames en uno solo
    df_final = pd.concat(dfs_procesados, ignore_index=True)
    
    # Generar tabla de totales 
    df_totales = generar_tabla_totales(df_final)
    
    logging.info("Transformación completada con éxito.")
    return df_final, df_totales