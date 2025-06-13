from app.db.conexion import ConexionDB
from app.models.comentarios import Comentario

class ComentarioDAO:
    INSERTAR = "INSERT INTO comentarios (contenido, fecha_creacion, usuario_id, tarea_id) VALUES (%s, %s, %s, %s) RETURNING id"
    LISTAR = "SELECT * FROM comentarios"
    BUSCAR_POR_ID = "SELECT * FROM comentarios WHERE id = %s"
    ACTUALIZAR = "UPDATE comentarios SET contenido = %s, fecha_creacion = %s, usuario_id = %s, tarea_id = %s WHERE id = %s"
    ELIMINAR = "DELETE FROM comentarios WHERE id = %s"

    @classmethod
    def insertar(cls, comentario: Comentario):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.INSERTAR, (
                        comentario.contenido,
                        comentario.fecha_creacion,
                        comentario.usuario_id,
                        comentario.tarea_id
                    ))
                    comentario.id = cursor.fetchone()[0]
                    return comentario
        except Exception as e:
            print(f"❌ Error al insertar comentario: {e}")
            return None
        finally:
            ConexionDB.liberar_conexion(conexion)

    @classmethod
    def listar(cls):
        conexion = ConexionDB.obtener_conexion()
        comentarios = []
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.LISTAR)
                    rows = cursor.fetchall()
                    for row in rows:
                        comentario = Comentario(id=row[0], contenido=row[1], fecha_creacion=row[2], usuario_id=row[3], tarea_id=row[4])
                        comentarios.append(comentario)
        except Exception as e:
            print(f"❌ Error al listar comentarios: {e}")
        finally:
            ConexionDB.liberar_conexion(conexion)
        return comentarios

    @classmethod
    def buscar_por_id(cls, id):
        conexion = ConexionDB.obtener_conexion()
        comentario = None
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.BUSCAR_POR_ID, (id,))
                    row = cursor.fetchone()
                    if row:
                        comentario = Comentario(id=row[0], contenido=row[1], fecha_creacion=row[2], usuario_id=row[3], tarea_id=row[4])
        except Exception as e:
            print(f"❌ Error al buscar comentario: {e}")
        finally:
            ConexionDB.liberar_conexion(conexion)
        return comentario

    @classmethod
    def actualizar(cls, comentario: Comentario):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.ACTUALIZAR, (
                        comentario.contenido,
                        comentario.fecha_creacion,
                        comentario.usuario_id,
                        comentario.tarea_id,
                        comentario.id
                    ))
                    return True
        except Exception as e:
            print(f"❌ Error al actualizar comentario: {e}")
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
            print(f"❌ Error al eliminar comentario: {e}")
            return False
        finally:
            ConexionDB.liberar_conexion(conexion)
