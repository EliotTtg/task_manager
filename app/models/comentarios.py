
class Comentario:
    def __init__(self, contenido, fecha, tarea_id, usuario_id, id=None):
        self._id = id
        self._contenido = contenido
        self._fecha = fecha
        self._tarea_id = tarea_id
        self._usuario_id = usuario_id

    def __str__(self):
        return f'Comentario: [id: {self._id}, contenido: {self._contenido}, fecha: {self._fecha}, tarea_id: {self._tarea_id}, usuario_id: {self._usuario_id}]'

    @property
    def id(self):
        return self._id

    @property
    def contenido(self):
        return self._contenido

    @property
    def fecha(self):
        return self._fecha

    @property
    def tarea_id(self):
        return self._tarea_id

    @property
    def usuario_id(self):
        return self._usuario_id

    @id.setter
    def id(self, id):
        self._id = id

    @contenido.setter
    def contenido(self, contenido):
        self._contenido = contenido

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @tarea_id.setter
    def tarea_id(self, tarea_id):
        self._tarea_id = tarea_id

    @usuario_id.setter
    def usuario_id(self, usuario_id):
        self._usuario_id = usuario_id


if __name__ == '__main__':

    comentario = Comentario(
        contenido='Buen avance en la tarea, solo falta el reporte final.',
        fecha='2025-06-16',
        tarea_id=1,
        usuario_id=1
    )
    print(comentario)