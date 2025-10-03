from fastapi import FastAPI, Body
from sqlmodel import SQLModel

app = FastAPI()

class Usuario(SQLModel):
    id: int
    nombre: str
    contraseña: str
    email: str
    actividad: bool

usuarios = [
    Usuario(id=1, nombre="Katty", contraseña="aa", email="katty@mail.com", actividad=True),
    Usuario(id=2, nombre="Kata",  contraseña="456", email="kata@mail.com", actividad=True),
    Usuario(id=3, nombre="Cris",  contraseña="789", email="cris@mail.com", actividad=False),
]
siguiente_id = 4

@app.post("/users/")
def create_user(nombre: str, contraseña: str, email: str, actividad: bool):
    global siguiente_id
    nuevo_usuario = Usuario(id=siguiente_id, nombre=nombre, contraseña=contraseña, email=email, actividad=actividad)
    usuarios.append(nuevo_usuario)
    siguiente_id += 1
    return {"message": "Usuario creado", "usuario": nuevo_usuario}

@app.get("/users/")
def listar_usuarios():
    return usuarios

@app.get("/users/{user_id}")
def obtener_usuario(user_id: int):
    for usuario in usuarios:
        if usuario.id == user_id:
            return usuario
    return {"error": "Usuario no encontrado"}

@app.put("/users/{user_id}")
def actualizar_usuario(user_id: int, nombre: str = None, contraseña: str = None, email: str = None, actividad: bool = None):
    for usuario in usuarios:
        if usuario.id == user_id:
            if nombre is not None:
                usuario.nombre = nombre
            if contraseña is not None:
                usuario.contraseña = contraseña
            if email is not None:
                usuario.email = email
            if actividad is not None:
                usuario.actividad = actividad
            return {"message": "Usuario actualizado", "usuario": usuario}
    return {"error": "Usuario no encontrado"}

@app.delete("/users/{user_id}")
def eliminar_usuario(user_id: int):
    for i, usuario in enumerate(usuarios):
        if usuario.id == user_id:
            usuarios.pop(i)
            return {"message": "Usuario eliminado"}
    return {"error": "Usuario no encontrado"}

@app.post("/login/")
def login(username: str = Body(...), password: str = Body(...)):
    for usuario in usuarios:
        if usuario.nombre == username and usuario.contraseña == password: 
            return {"message": "Login exitoso"}
    return {"message": "Login fallido"}