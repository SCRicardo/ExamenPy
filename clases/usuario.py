from conexion_mongo import ConexionMongo

class Usuario:
    def __init__(self, nombre, email, password, id_grupo):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.id_grupo = id_grupo


    def verificar_grupo_cliente(func):
        def wrapper(usuario):
            if usuario.id_grupo == 100:
                return func(usuario)
            else:
                print("Acceso denegado: el usuario no pertenece al grupo de clientes.")
                return None  # O puedes lanzar una excepción

        return wrapper


    @verificar_grupo_cliente
    def ver_carrito(usuario):
        print(f"Mostrando el carrito de {usuario.nombre}...")
        # Aquí iría la lógica para mostrar el carrito.


#usuario_cliente = Usuario("Juan Perez", "juan@example.com", "mypassword", 200)
#ver_carrito(usuario_cliente)  # Esto debería mostrar el carrito

"""
# Código para registrar un usuario al ejecutar este archivo
if __name__ == "__main__":
    # Conectar a MongoDB
    conexion = ConexionMongo()
    db = conexion.get_db()

    # Crear instancia del gestor de usuarios
    gestor_usuarios = GestorUsuarios(db)

    # Registrar un usuario
    gestor_usuarios.registrar_usuario("Juan Perez", "juan@example.com", "mypassword", 100)

    print("Usuario registrado: Juan Perez, Grupo ID: 100")
"""

