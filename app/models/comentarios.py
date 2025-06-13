from usuarios import Usuario

class Comentario:
    def __init__(self,titulo,descripcion,estado,fecha_creacion,fecha_limite,usuario_id,id = None):
        self._id = id
        self._titulo = titulo
        self._descripcion = descripcion
        self._estado = estado
        self._fecha_creacion = fecha_creacion
        self._fecha_limite = fecha_limite
        self._usuario_id = usuario_id
        
    def __str__(self):
        return f'Comentario: [id: {self._id}, titulo: {self._titulo}, descripcion: {self._descripcion}, estado: {self._estado}, fecha_creacion: {self._fecha_creacion}, fecha_limite: {self._fecha_limite}, usuario_id: {self._usuario_id}]'
    
    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def estado(self):
        return self._estado

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @property
    def fecha_limite(self):
        return self._fecha_limite

    @property
    def usuario_id(self):
        return self._usuario_id

    @id.setter
    def id(self, id):
        self._id = id

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion):
        self._fecha_creacion = fecha_creacion

    @fecha_limite.setter
    def fecha_limite(self, fecha_limite):
        self._fecha_limite = fecha_limite

    @usuario_id.setter
    def usuario_id(self, usuario_id):
        self._usuario_id = usuario_id


if __name__ == '__main__':
    usuario1 = Usuario('Eliot', 'eliot@gmail.com', '123456', id=1)
    print(usuario1)

    comentario = Comentario(
        titulo='Estudiar Flask',
        descripcion='Repasar rutas y conexión con base de datos',
        estado='pendiente',
        fecha_creacion='2025-06-13',
        fecha_limite='2025-06-20',
        usuario_id=usuario1.id
    )
    print(comentario)