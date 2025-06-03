from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import Base
from repositories.user_repository import UsuarioRepository
from services.user_services import UsuarioService
import os

# Crear carpeta para la base de datos si no existe
os.makedirs("data", exist_ok=True)

# Ruta y configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./data/database.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Crear repositorio y servicio
usuario_repo = UsuarioRepository(session)
usuario_service = UsuarioService(usuario_repo)

def menu():
    while True:
        print("\n--- CRUD de Usuarios ---")
        print("1. Crear usuario")
        print("2. Ver usuario por ID")
        print("3. Ver todos los usuarios")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                edad = int(input("Edad: "))
                usuario = usuario_service.crear_usuario(nombre, email, edad)
                print("✅ Usuario creado:", usuario.__dict__)

            elif opcion == "2":
                user_id = int(input("ID del usuario: "))
                usuario = usuario_service.obtener_usuario(user_id)
                print(usuario.__dict__ if usuario else "❌ No encontrado")

            elif opcion == "3":
                usuarios = usuario_service.obtener_usuarios()
                for u in usuarios:
                    print(u.__dict__)

            elif opcion == "4":
                user_id = int(input("ID del usuario: "))
                campo = input("Campo a actualizar (nombre/email/edad): ")
                valor = input("Nuevo valor: ")
                if campo == "edad":
                    valor = int(valor)
                actualizado = usuario_service.actualizar_usuario(user_id, {campo: valor})
                print(actualizado.__dict__ if actualizado else "❌ No encontrado")

            elif opcion == "5":
                user_id = int(input("ID del usuario a eliminar: "))
                eliminado = usuario_service.eliminar_usuario(user_id)
                print("🗑️ Eliminado" if eliminado else "❌ No encontrado")

            elif opcion == "0":
                print("👋 Saliendo del programa.")
                break
            else:
                print("⚠️ Opción inválida.")
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    menu()
