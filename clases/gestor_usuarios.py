from conexion_mongo import ConexionMongo
from grupo import Grupo
from usuario import Usuario

class GestorUsuarios:
    def __init__(self, db):
        self.db = db

    def registrar_usuario(self, nombre, email, password, id_grupo):
        from usuario import Usuario  # Importar localmente aquí
        usuario = Usuario(nombre, email, password, id_grupo)
        self.db.usuarios.insert_one(vars(usuario))

    def obtener_usuario_por_email(self, email):
        usuario_data = self.db.usuarios.find_one({"email": email})
        if usuario_data:
            from usuario import Usuario  # Importar localmente aquí
            return Usuario(usuario_data['nombre'], usuario_data['email'], usuario_data['password'], usuario_data['id_grupo'])
        return None

    def buscar_grupo_por_id(self, id_grupo):
        # Buscar por el campo id_grupo en lugar de _id
        grupo_data = self.db.grupos.find_one({"id_grupo": id_grupo})
        if grupo_data:
            return Grupo(grupo_data['id_grupo'], grupo_data['nombre'], grupo_data['permisos'])
        return None


if __name__ == "__main__":
    # Conectar a MongoDB
    conexion = ConexionMongo()
    db = conexion.get_db()

    # Crear instancia del gestor de usuarios
    gestor_usuarios = GestorUsuarios(db)

    # Registrar un usuario de ejemplo (solo si no está registrado)
    usuario_email = "juan@example.com"
    usuario_existente = gestor_usuarios.obtener_usuario_por_email(usuario_email)

    if usuario_existente is None:
        gestor_usuarios.registrar_usuario("Juan Perez", usuario_email, "mypassword", 100)
        print(f"Usuario registrado: Juan Perez, Grupo ID: 100")
    else:
        print(f"El usuario ya existe: {usuario_existente.nombre}, Grupo ID: {usuario_existente.id_grupo}")

    # Buscar usuario por email
    usuario_encontrado = gestor_usuarios.obtener_usuario_por_email("pedro@example.com")
    if usuario_encontrado:
        print(f"Usuario encontrado: {usuario_encontrado.nombre}, Email: {usuario_encontrado.email}, Grupo ID: {usuario_encontrado.id_grupo}")
        usuario_cliente = Usuario(usuario_encontrado.nombre, usuario_encontrado.email,"", usuario_encontrado.id_grupo)
        obj=Usuario
        obj.ver_carrito(usuario_cliente)  # Esto debería mostrar el carrito
    else:
        print("Usuario no encontrado.")

    # Buscar grupo por ID
    grupo_id = 100
    grupo_encontrado = gestor_usuarios.buscar_grupo_por_id(grupo_id)
    if grupo_encontrado:
        print(f"Grupo encontrado: {grupo_encontrado.nombre}, ID: {grupo_encontrado.id_grupo}, Permisos: {grupo_encontrado.permisos}")
    else:
        print("Grupo no encontrado.")

