# db.py
from psycopg2 import pool
import atexit

class ConexionDB:
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    1, 10,
                    user='postgres',
                    password='admin',
                    host='127.0.0.1',
                    port='5432',
                    database='test_db'
                )
                print("✅ Pool de conexiones creado con éxito.")
            except Exception as e:
                print(f"❌ Error al crear el pool: {e}")
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
            print("✅ Cerrando conexiones del pool...")  # ← Este es el mensaje que se muestra
            cls._pool.closeall()
            
atexit.register(ConexionDB.cerrar_todo)
