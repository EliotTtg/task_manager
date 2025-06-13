from app.db.conexion import ConexionDB
from app.models.tareas import Tarea

class TareaDAO:
    INSERTAR = '''
        INSERT INTO tareas (titulo, descripcion, estado, fecha_creacion, fecha_limite, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
    '''
    SELECCIONAR = 'SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_limite, usuario_id FROM tareas ORDER BY id'
    ACTUALIZAR = '''
        UPDATE tareas
        SET titulo = %s, descripcion = %s, estado = %s, fecha_creacion = %s, fecha_limite = %s, usuario_id = %s
        WHERE id = %s
    '''
    ELIMINAR = 'DELETE FROM tareas WHERE id = %s'
    BUSCAR_POR_ID = 'SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_limite, usuario_id FROM tareas WHERE id = %s'

    @classmethod
    def insertar(cls, tarea: Tarea):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.INSERTAR, (
                        tarea.titulo, tarea.descripcion, tarea.estado,
                        tarea.fecha_creacion, tarea.fecha_limite, tarea.usuario_id
                    ))
                    tarea.id = cursor.fetchone()[0]
                    return tarea
        except Exception as e:
            print(f"❌ Error al insertar tarea: {e}")
            return None
        finally:
            ConexionDB.liberar_conexion(conexion)

    @classmethod
    def listar(cls):
        conexion = ConexionDB.obtener_conexion()
        tareas = []
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.SELECCIONAR)
                    registros = cursor.fetchall()
                    for fila in registros:
                        tarea = Tarea(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[0])
                        tareas.append(tarea)
        except Exception as e:
            print(f"❌ Error al listar tareas: {e}")
        finally:
            ConexionDB.liberar_conexion(conexion)
        return tareas

    @classmethod
    def actualizar(cls, tarea: Tarea):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.ACTUALIZAR, (
                        tarea.titulo, tarea.descripcion, tarea.estado,
                        tarea.fecha_creacion, tarea.fecha_limite,
                        tarea.usuario_id, tarea.id
                    ))
                    return cursor.rowcount
        except Exception as e:
            print(f"❌ Error al actualizar tarea: {e}")
            return 0
        finally:
            ConexionDB.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_tarea: int):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.ELIMINAR, (id_tarea,))
                    return cursor.rowcount
        except Exception as e:
            print(f"❌ Error al eliminar tarea: {e}")
            return 0
        finally:
            ConexionDB.liberar_conexion(conexion)

    @classmethod
    def buscar_por_id(cls, id_tarea: int):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.BUSCAR_POR_ID, (id_tarea,))
                    fila = cursor.fetchone()
                    if fila:
                        return Tarea(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[0])
                    return None
        except Exception as e:
            print(f"❌ Error al buscar tarea por ID: {e}")
            return None
        finally:
            ConexionDB.liberar_conexion(conexion)
