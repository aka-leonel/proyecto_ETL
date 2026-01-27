-- Tabla principal unificada 
CREATE TABLE IF NOT EXISTS info_cultural (
    id SERIAL PRIMARY KEY,
    cod_localidad INT,
    id_provincia INT,
    id_departamento INT,
    categoria VARCHAR(100),
    provincia VARCHAR(100),
    localidad VARCHAR(100),
    nombre VARCHAR(255),
    domicilio TEXT,
    codigo_postal VARCHAR(20),
    numero_de_telefono VARCHAR(50),
    mail VARCHAR(100),
    web TEXT,
    fecha_carga DATE 
);

-- Tabla de totales 
CREATE TABLE IF NOT EXISTS totales_procesados (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(255), 
    categoria VARCHAR(100),
    provincia VARCHAR(100),
    cantidad INT,
    fecha_carga DATE 
);