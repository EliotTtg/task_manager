from fastapi import APIRouter,HTTPException
from pydantic import BaseModel, EmailStr,Field
from typing import Optional
from app.dao.usuario_dao import UsuarioDAO
from app.models.usuarios import Usuario

appUsuario = APIRouter()

class UsuarioSchema(BaseModel):  # Modelo de entrada (request)
    id: Optional[int] = None
    nombre: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=6)

class UsuarioOutSchema(BaseModel):  # Modelo de salida (response)
    id: int
    nombre: str
    email: EmailStr

    class Config:
        from_attributes = True    
    
    
@appUsuario.get("/")
def listar_usuarios():
    lista = UsuarioDAO.listar()
    return {"message": "Lista de usuarios","usuarios":[UsuarioSchema.from_orm(u).model_dump() for u in lista]}

@appUsuario.post("/")
def agregar_usuario(usuario:UsuarioSchema):
    try:
        userInsert = UsuarioDAO.insertar(usuario)
    
        if userInsert is None:
            raise HTTPException(status_code=500, detail="Error al crear el usuario")
        
        return {"message": "Usuario creado","usuario":{
            "id":userInsert.id,
            "nombre":userInsert.nombre,
            "email":userInsert.email,
            "password":userInsert.password
            }
        }
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
@appUsuario.put("/{id}")
def actualizar_usuario(id:int,usuario:UsuarioSchema):
    try:
        usuarioI = Usuario(id=id,nombre=usuario.nombre,email=usuario.email,password=usuario.password)
        userUpdate = UsuarioDAO.actualizar(usuarioI)
        
        if userUpdate is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        return {"message": "Usuario actualizado","usuario":{
            "id":usuarioI.id,
            "nombre":usuarioI.nombre,
            "email":usuarioI.email,
            "password":usuarioI.password
            }
        }
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
@appUsuario.delete("/{id}")
def eliminar_usuario(id:int):
    try:
        userDelete = UsuarioDAO.eliminar(id)
        if userDelete is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        return {"message": "Usuario eliminado","usuario":{
            "id":id}
        }
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
