class Categoria:
    def __init__(self,nombre,id = None):
        self._id = id
        self._nombre = nombre
        
    def __str__(self):
        return f'Categoria: [id: {self._id}, nombre: {self._nombre}]'
    
    @property
    def id(self):
        return self._id
        
    @property
    def nombre(self):
        return self._nombre
    
    @id.setter
    def id(self,id):
        self._id = id
        
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
        

if __name__ == '__main__':
    categoria = Categoria('Eliot','1')
    print(categoria)