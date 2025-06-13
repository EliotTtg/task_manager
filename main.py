from app.dao.usuario_dao import UsuarioDAO
from app.models.usuarios import Usuario

usuario = Usuario('pablo','jorge@gmail.com','123456')

print(UsuarioDAO.insertar(usuario))