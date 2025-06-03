import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import Base, Usuario
from repositories.user_repository import UsuarioRepository
from services.user_service import UsuarioService

# Usar una base de datos en memoria para pruebas
@pytest.fixture(scope="function")
def session():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture(scope="function")
def servicio(session):
    repo = UsuarioRepository(session)
    return UsuarioService(repo)

def test_crear_usuario(servicio):
    usuario = servicio.crear_usuario("Juan", "juan@example.com", 25)
    assert usuario.id is not None
    assert usuario.nombre == "Juan"

def test_crear_usuario_datos_invalidos(servicio):
    with pytest.raises(ValueError):
        servicio.crear_usuario("", "invalido", "edad_no_entero")

def test_obtener_usuario(servicio):
    creado = servicio.crear_usuario("Ana", "ana@example.com", 30)
    encontrado = servicio.obtener_usuario(creado.id)
    assert encontrado.email == "ana@example.com"

def test_obtener_usuarios(servicio):
    servicio.crear_usuario("Pedro", "pedro@example.com", 40)
    servicio.crear_usuario("Laura", "laura@example.com", 35)
    usuarios = servicio.obtener_usuarios()
    assert len(usuarios) == 2

def test_actualizar_usuario(servicio):
    usuario = servicio.crear_usuario("Carlos", "carlos@example.com", 50)
    actualizado = servicio.actualizar_usuario(usuario.id, {"nombre": "Carlos A."})
    assert actualizado.nombre == "Carlos A."

def test_eliminar_usuario(servicio):
    usuario = servicio.crear_usuario("Luis", "luis@example.com", 28)
    eliminado = servicio.eliminar_usuario(usuario.id)
    assert eliminado is not None
    assert servicio.obtener_usuario(usuario.id) is None
