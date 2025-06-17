
from fastapi import FastAPI
from app.router.usuarios_router import appUsuario

app = FastAPI(
    title='API TASK_MANAGER',
    description='Este es un sistema básico de gestión de tareas usando Python, PostgreSQL y una estructura organizada en capas: modelos, DAOs y conexión a base de datos.',
    version='0.0.1'
)

app.include_router(appUsuario, prefix="/usuarios", tags=["Usuarios"])

@app.get("/",include_in_schema=False)
def home():
    return {"github":"https://github.com/EliotTtg"}