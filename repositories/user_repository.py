from models.user import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def crear(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def obtener_por_id(self, user_id: int):
        return self.session.query(Usuario).filter_by(id=user_id).first()

    def obtener_todos(self):
        return self.session.query(Usuario).all()

    def actualizar(self, user_id: int, nuevos_datos: dict):
        usuario = self.obtener_por_id(user_id)
        if usuario:
            for key, value in nuevos_datos.items():
                setattr(usuario, key, value)
            self.session.commit()
        return usuario

    def eliminar(self, user_id: int):
        usuario = self.obtener_por_id(user_id)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
        return usuario
