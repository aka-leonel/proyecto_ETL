import logging
from sqlalchemy import create_engine, text
from decouple import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def obtener_engine():
    try:
        user = config('DB_USER')
        password = config('DB_PASS')
        host = config('DB_HOST')
        port = config('DB_PORT')
        db_name = config('DB_NAME')
        
        url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
        return create_engine(url)
    except Exception as e:
        logging.error(f"Error al configurar la conexión: {e}")
        return None

def ejecutar_sql_script(ruta_sql):
    """
    Lee y ejecuta un archivo .sql para crear las tablas.
    """
    engine = obtener_engine()
    if engine:
        try:
            with open(ruta_sql, 'r') as f:
                query = text(f.read())
            
            with engine.connect() as conn:
                conn.execute(query)
                conn.commit()
            logging.info(f"Script SQL {ruta_sql} ejecutado correctamente.")
        except Exception as e:
            logging.error(f"Error al ejecutar el script SQL: {e}")

def cargar_datos(df, nombre_tabla):
    """
    Carga los datos reemplazando la información previa.
    """
    engine = obtener_engine()
    if engine:
        try:
            # Reemplazamos los datos. 'replace' de pandas recrea la tabla, 
            # pero como ya ejecutamos el SQL, 'replace' es seguro aquí.
            df.to_sql(nombre_tabla, engine, if_exists='replace', index=False)
            logging.info(f"Tabla '{nombre_tabla}' cargada exitosamente.")
        except Exception as e:
            logging.error(f"Error al cargar la tabla {nombre_tabla}: {e}")