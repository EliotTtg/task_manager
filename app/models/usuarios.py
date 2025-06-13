class Usuario:
    def __init__(self,nombre,email,password,id = None):
        self._id = id
        self._nombre = nombre
        self._email = email
        self._password = password
        
    def __str__(self):
        return f'Usuario: [id: {self._id}, nombre: {self._nombre}, email: {self.email}, password: {self._password}]'
    
    @property
    def id(self):
        return self._id
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def email(self):
        return self._email
    
    @property
    def password(self):
        return self._password
    
    @id.setter
    def id(self,id):
        self._id = id
        
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
        
    
    @email.setter
    def email(self,email):
        self._email = email
    
    @password.setter
    def password(self,password):
        self._password = password
        

if __name__ == '__main__':
    usuario1 = Usuario('Eliot','eliot@gmail.com','123456')
    print(usuario1)

    