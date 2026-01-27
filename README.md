# proyecto_ETL: Challenge Data Analytics - Python (Alkemy)

Este proyecto es un pipeline ETL que automatiza la extracción, transformación y carga de datos culturales de Argentina (Museos y Bibliotecas) en una base de datos PostgreSQL.

## 🚀 Instalación y Setup

### 1. Clonar el repositorio
git clone https://github.com/aka-leonel/proyecto_ETL.git
cd proyecto_ETL

### 2. Configurar el Entorno Virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Instalar y Configurar la Base de Datos (PostgreSQL)
En Linux Fedora: sudo dnf install postgresql-server
En Ubuntu: sudo apt install postgresql

Iniciar servicio: sudo systemctl start postgresql.

Crear DB:
sudo -u postgres psql
CREATE DATABASE cultura_db;
CREATE USER mi_usuario WITH PASSWORD 'mi_password';
GRANT ALL PRIVILEGES ON DATABASE cultura_db TO mi_usuario;

En Windows
Descargar el instalador desde postgresql.org.
Durante la instalación, anotar la contraseña del usuario postgres.
Abrir pgAdmin 4, crear una base de datos llamada cultura_db.

### 4. Variables de Entorno
Crea un archivo .env en la raíz con tus credenciales:
DB_USER=mi_usuario
DB_PASS=mi_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cultura_db

### 🛠️ Ejecución
Ejecuta el pipeline completo por consola:
Si no ves el (venv) en la terminal, actívalo primero:
source venv/bin/activate
Instala todo lo que definimos en el requirements.txt:
pip install -r requirements.txt

Ejecuta el archivo principal:
python3 main.py

#### ⚙️ Cómo Adaptar a Nuevas Fuentes
Para usar este proyecto con otros archivos CSV o cambiar el mapeo de columnas, edita el archivo config.py:

SOURCES: Agrega o modifica las URLs de los archivos CSV.

COLUMN_MAPPING: Si el nuevo CSV tiene nombres de columnas distintos (ej: "Phone" en lugar de "Teléfono"), agrega la relación: 'Phone': 'número de teléfono'.

FINAL_COLUMNS: Define qué columnas quieres que lleguen finalmente a la base de datos.