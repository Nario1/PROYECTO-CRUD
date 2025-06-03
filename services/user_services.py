from models.user import Usuario
from repositories.user_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def crear_usuario(self, nombre, email, edad):
        if not nombre or not email or not isinstance(edad, int):
            raise ValueError("Datos inválidos")
        usuario = Usuario(nombre=nombre, email=email, edad=edad)
        return self.repo.crear(usuario)

    def obtener_usuario(self, user_id):
        return self.repo.obtener_por_id(user_id)

    def obtener_usuarios(self):
        return self.repo.obtener_todos()

    def actualizar_usuario(self, user_id, nuevos_datos):
        return self.repo.actualizar(user_id, nuevos_datos)

    def eliminar_usuario(self, user_id):
        return self.repo.eliminar(user_id)
