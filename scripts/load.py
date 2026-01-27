import logging
from sqlalchemy import create_engine
from decouple import config

# Configuración de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def obtener_engine():
    """
    Crea la conexión a la base de datos usando variables de entorno.
    """
    try:
        user = config('DB_USER')
        password = config('DB_PASS')
        host = config('DB_HOST')
        port = config('DB_PORT')
        db_name = config('DB_NAME')
        
        # URL de conexión para PostgreSQL
        url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
        engine = create_engine(url)
        return engine
    except Exception as e:
        logging.error(f"Error al configurar la conexión: {e}")
        return None

def cargar_datos(df, nombre_tabla):
    """
    Carga un DataFrame a la base de datos reemplazando los datos previos.
    """
    engine = obtener_engine()
    if engine:
        try:
            # Reemplaza los registros existentes con if_exists='replace' 
            df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)
            logging.info(f"Tabla '{nombre_tabla}' cargada exitosamente.")
        except Exception as e:
            logging.error(f"Error al cargar la tabla {nombre_tabla}: {e}")