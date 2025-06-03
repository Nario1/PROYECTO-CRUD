# 🗃️ Proyecto CRUD con SQLAlchemy y SQLite
Este proyecto implementa un sistema completo de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para la entidad `Usuario`, usando Python, SQLAlchemy como ORM, y SQLite como base de datos local. Está organizado siguiendo una arquitectura por capas para mantener una estructura limpia y escalable.
---
## 🚀 Tecnologías Usadas
- 🐍 Python 3.11+
- 🧮 SQLAlchemy (ORM)
- 🗃️ SQLite (almacenada en `./data/database.db`)
- 🧪 pytest / unittest (para pruebas unitarias)
---
## 🧱 Estructura del Proyecto
proyecto/
├── models/             # Entidades y esquemas de la base de datos
├── repositories/       # Capa de acceso a datos (CRUD)
├── services/           # Lógica de negocio
├── tests/              # Pruebas unitarias
├── data/               # Base de datos SQLite (se genera automáticamente)
├── main.py             # Punto de entrada principal
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación del proyecto
---
## 📦 Instalación y Uso
1. **Clonar el repositorio** (reemplaza `Nario1` por tu usuario GitHub):
git clone https://github.com/Nario1/proyecto-crud-sqlalchemy.git
cd proyecto-crud-sqlalchemy
2. **Crear entorno virtual y activarlo**:
- En Windows:
python -m venv venv
venv\Scripts\activate
- En macOS/Linux:
python3 -m venv venv
source venv/bin/activate
3. **Instalar dependencias**:
pip install -r requirements.txt
4. **Ejecutar la aplicación**:
python main.py
---
## 🧪 Ejecutar Pruebas
Las pruebas unitarias están en la carpeta `tests/` y usan una base de datos en memoria para evitar afectar la base de datos real.
- Con pytest:
pytest
- Con unittest:
python -m unittest discover -s tests
---
## 🧭 Modelo Conceptual (Usuario)
+------------+
|  Usuario   |
+------------+
| id: int    |
| nombre: str|
| email: str |
| edad: int  |
+------------+
---
✍️ Autor y Licencia  
Licencia: MIT  
🔗 Repositorio: https://github.com/Nario1/proyecto-crud-sqlalchemy
