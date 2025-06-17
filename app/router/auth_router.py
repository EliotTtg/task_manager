from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr,Field
from typing import Optional
from app.dao.usuario_dao import UsuarioDAO
from app.models.usuarios import Usuario
from app.auth.security import createToken

appAuth = APIRouter()

class UsuarioSchema(BaseModel):  # Modelo de entrada (request)
    email: EmailStr
    password: str = Field(min_length=6)

class UsuarioOutSchema(BaseModel):  # Modelo de salida (response)
    nombre: str
    email: EmailStr

    class Config:
        from_attributes = True    
    
    
@appAuth.post("/login")
def login(usuario:UsuarioSchema):
    if usuario.email == 'cristopher@gmail.com' and usuario.password == '123456':
        token: str = createToken(usuario.dict())
        return JSONResponse(content=token)
    