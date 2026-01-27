# URLs de las fuentes de datos
SOURCES = {
    'museos': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv',
    'bibliotecas': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/bibliotecas-populares.csv'
}

# Columnas requeridas según la consigna
FINAL_COLUMNS = [
    'cod_localidad', 'id_provincia', 'id_departamento', 'categoria', 'provincia', 'localidad', 'nombre', 'domicilio', 'codigo_postal', 'numero_de_telefono', 'mail', 'web'
]

# Mapeo de columnas para normalización
# Aquí definimos: { 'columna_en_el_csv_original': 'columna_final_en_la_db' }
COLUMN_MAPPING = {
    'Cod_Loc': 'cod_localidad',
    'IdProvincia': 'id_provincia',
    'IdDepartamento': 'id_departamento',
    'categoría': 'categoria',
    'provincia': 'provincia',
    'localidad': 'localidad',
    'nombre': 'nombre',
    'domicilio': 'domicilio',
    'CP': 'codigo_postal',
    'teléfono': 'numero_de_telefono',
    'Mail': 'mail',
    'Web': 'web',
    # Agregar aquí variaciones para bibliotecas si son distintas
    'Cod_loc': 'cod_localidad',
    'Categoría': 'categoria',
    'Provincia': 'provincia',
    'Localidad': 'localidad',
    'Nombre': 'nombre',
    'Domicilio': 'domicilio',
    'Teléfono': 'numero_de_telefono'
}