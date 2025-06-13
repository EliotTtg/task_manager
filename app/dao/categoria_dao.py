from app.db.conexion import ConexionDB
from app.models.categorias import Categoria

class CategoriaDAO:
    INSERTAR = "INSERT INTO categorias (nombre) VALUES (%s) RETURNING id"
    LISTAR = "SELECT * FROM categorias"
    BUSCAR_POR_ID = "SELECT * FROM categorias WHERE id = %s"
    ACTUALIZAR = "UPDATE categorias SET nombre = %s WHERE id = %s"
    ELIMINAR = "DELETE FROM categorias WHERE id = %s"

    @classmethod
    def insertar(cls, categoria: Categoria):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.INSERTAR, (categoria.nombre,))
                    categoria.id = cursor.fetchone()[0]
                    return categoria
        except Exception as e:
            print(f"❌ Error al insertar categoría: {e}")
            return None
        finally:
            ConexionDB.liberar_conexion(conexion)

    @classmethod
    def listar(cls):
        conexion = ConexionDB.obtener_conexion()
        categorias = []
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.LISTAR)
                    rows = cursor.fetchall()
                    for row in rows:
                        categoria = Categoria(id=row[0], nombre=row[1])
                        categorias.append(categoria)
        except Exception as e:
            print(f"❌ Error al listar categorías: {e}")
        finally:
            ConexionDB.liberar_conexion(conexion)
        return categorias

    @classmethod
    def buscar_por_id(cls, id):
        conexion = ConexionDB.obtener_conexion()
        categoria = None
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.BUSCAR_POR_ID, (id,))
                    row = cursor.fetchone()
                    if row:
                        categoria = Categoria(id=row[0], nombre=row[1])
        except Exception as e:
            print(f"❌ Error al buscar categoría: {e}")
        finally:
            ConexionDB.liberar_conexion(conexion)
        return categoria

    @classmethod
    def actualizar(cls, categoria: Categoria):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.ACTUALIZAR, (categoria.nombre, categoria.id))
                    return True
        except Exception as e:
            print(f"❌ Error al actualizar categoría: {e}")
            return False
        finally:
            ConexionDB.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.ELIMINAR, (id,))
                    return cursor.rowcount > 0
        except Exception as e:
            print(f"❌ Error al eliminar categoría: {e}")
            return False
        finally:
            ConexionDB.liberar_conexion(conexion)
