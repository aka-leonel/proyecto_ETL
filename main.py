import logging
from scripts.extract import ejecutar_extraccion
from scripts.transform import ejecutar_transformacion
from scripts.load import cargar_datos, ejecutar_sql_script

# Configuración centralizada de Logs 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ejecucion.log"),
        logging.StreamHandler()
    ]
)

def main():
    logging.info("Iniciando proceso ETL...")

    try:
        # 0. PREPARACIÓN DE TABLAS (Requerimiento Técnico )
        logging.info("Preparando tablas en la base de datos...")
        ejecutar_sql_script("database/create_tables.sql")

        # 1. EXTRACCIÓN
        rutas_archivos = ejecutar_extraccion()
        if not rutas_archivos:
            logging.error("No se pudieron obtener los archivos fuente. Abortando.")
            return

        # 2. TRANSFORMACIÓN
        df_unificado, df_totales = ejecutar_transformacion(rutas_archivos)

        # 3. CARGA [cite: 65, 66]
        logging.info("Cargando datos en PostgreSQL...")
        cargar_datos(df_unificado, 'info_cultural')
        cargar_datos(df_totales, 'totales_procesados')

        logging.info("Proceso ETL finalizado exitosamente.")

    except Exception as e:
        logging.error(f"Error crítico en la ejecución: {e}", exc_info=True)

if __name__ == "__main__":
    main()