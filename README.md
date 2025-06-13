# 🐍 Proyecto de Gestión de Tareas en Python + PostgreSQL

Este es un sistema básico de gestión de tareas usando Python, PostgreSQL y una estructura organizada en capas: modelos, DAOs y conexión a base de datos.

---

## 📦 Estructura del Proyecto

```
mi_proyecto/
│
├── app/                        # Lógica principal
│   ├── models/                 # Clases de entidades (Usuario, Tarea, Categoria, etc.)
│   │   ├── usuario.py
│   │   ├── tarea.py
│   │   ├── categoria.py
│   │   └── comentarios.py
│   │
│   ├── dao/                    # Clases DAO (acceso a base de datos)
│   │   ├── usuario_dao.py
│   │   ├── tarea_dao.py
│   │   ├── categoria_dao.py
│   │   └── comentarios_dao.py
│   │
│   ├── db/                     # Conexión con PostgreSQL
│   │   └── conexion.py
│   │
│   ├── router/                 # (Futuro) Rutas si usas Flask/FastAPI
│   │   └── tarea_router.py
│   │
│   ├── static/                 # (Futuro) Archivos estáticos (CSS, JS, imágenes)
│   │   └── style.css
│   │
│   ├── templates/              # (Futuro) HTML con Jinja2 o motor de plantillas
│   │   └── index.html
│   │
│   ├── main.py                 # Punto de entrada de la app (puede incluir pruebas o app.run)
│   └── utils/                  # (Opcional) Funciones auxiliares
│
├── venv/                       # Entorno virtual (no se sube al repositorio)
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Descripción del proyecto

```

---

## ⚙️ Requisitos

- Python 3.10 o superior
- PostgreSQL instalado y corriendo
- Instalar las dependencias con:

```bash
pip install psycopg2
```

> Si usas `psycopg2-binary`, también funcionará para desarrollo:
```bash
pip install psycopg2-binary
```

---

## 🛠️ Configuración de la base de datos

1. Crea una base de datos llamada `test_db` en PostgreSQL.
2. Asegúrate de tener el usuario y contraseña correctos en `app/db/conexion.py`.

```python
# Ejemplo de conexión (conexion.py)

from psycopg2 import pool
import atexit

class ConexionDB:
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            cls._pool = pool.SimpleConnectionPool(
                1, 10,
                user='postgres',
                password='admin',
                host='127.0.0.1',
                port='5432',
                database='test_db'
            )
        return cls._pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().getconn()

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)

    @classmethod
    def cerrar_todo(cls):
        if cls._pool:
            print("✅ Cerrando conexiones del pool...")
            cls._pool.closeall()

atexit.register(ConexionDB.cerrar_todo)
```

---

## 📚 Descripción de Carpetas

- **models/**  
  Contiene las clases que representan las entidades: `Usuario`, `Tarea`, `Categoria`, etc.

- **dao/**  
  Clases DAO que manejan el acceso a la base de datos (insertar, actualizar, eliminar, listar).

- **db/**  
  Gestión de la conexión a PostgreSQL utilizando `SimpleConnectionPool`.

- **main.py**  
  Script para ejecutar pruebas o correr la aplicación.

---

## 🚀 ¿Cómo ejecutar?

```bash
python app/main.py
```

---

## 🧠 Ejemplo de uso (insertar usuario)

```python
from app.models.usuario import Usuario
from app.dao.usuario_dao import UsuarioDAO

usuario = Usuario(nombre='Eliot', email='eliot@gmail.com', password='123456')
UsuarioDAO.insertar(usuario)
```

---

## ✅ Buenas prácticas implementadas

- Separación de responsabilidades (DAO / modelo / conexión)
- Encapsulamiento de datos con `@property`
- Uso de `atexit` para cerrar conexiones automáticamente
- Preparación para crecer hacia una API o interfaz web

---

## 🙌 Autor

- Eliot 😎
