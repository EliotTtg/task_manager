
from app.models.usuarios import Usuario
from app.db.conexion import ConexionDB

class UsuarioDAO:
    
    INSERTAR = 'INSERT INTO usuarios(nombre, email, password) VALUES (%s, %s, %s) RETURNING id'
    SELECCIONAR = 'SELECT id, nombre, email, password FROM usuarios ORDER BY id'
    ACTUALIZAR = 'UPDATE usuarios SET nombre=%s, email=%s, password=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM usuarios WHERE id = %s'
    BUSCAR_POR_ID = 'SELECT id, nombre, email, password FROM usuarios WHERE id = %s'

    
    @classmethod
    def insertar(cls, usuario: Usuario):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.INSERTAR, (usuario.nombre, usuario.email, usuario.password))
                    usuario.id = cursor.fetchone()[0]
                    return usuario
        except Exception as e:
            print(f"❌ Error al insertar usuario: {e}")
            return None
        finally:
            ConexionDB.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, usuario: Usuario):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.ACTUALIZAR,(usuario.nombre, usuario.email, usuario.password,usuario.id))
                    return cursor.rowcount
        except Exception as e:
            print(f"❌ Error al actualizar usuario: {e}")
            return 0
        finally:
            ConexionDB.liberar_conexion(conexion)
            
    @classmethod
    def eliminar(cls, id_usuario: int):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.ELIMINAR, (id_usuario,))
                    return cursor.rowcount
        except Exception as e:
            print(f"❌ Error al eliminar usuario: {e}")
            return 0
        finally:
            ConexionDB.liberar_conexion(conexion)
            
    @classmethod
    def listar(cls):
        conexion = ConexionDB.obtener_conexion()
        usuarios = []
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.SELECCIONAR)
                    registros = cursor.fetchall()
                    for fila in registros:
                        usuario = Usuario(fila[1], fila[2], fila[3], fila[0])
                        usuarios.append(usuario)
        except Exception as e:
            print(f"❌ Error al listar usuarios: {e}")
        finally:
            ConexionDB.liberar_conexion(conexion)
        return usuarios
    
    @classmethod
    def buscar_por_id(cls, id_usuario: int):
        conexion = ConexionDB.obtener_conexion()
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls.BUSCAR_POR_ID, (id_usuario,))
                    fila = cursor.fetchone()
                    if fila:
                        return Usuario(fila[1], fila[2], fila[3], fila[0])
                    return None
        except Exception as e:
            print(f"❌ Error al buscar usuario por ID: {e}")
            return None
        finally:
            ConexionDB.liberar_conexion(conexion)