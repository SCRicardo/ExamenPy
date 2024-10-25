class Grupo:
    def __init__(self, id_grupo, nombre, permisos):
        self.id_grupo = id_grupo
        self.nombre = nombre
        self.permisos = permisos

    def tiene_permiso(self, permiso):
        return permiso in self.permisos

from conexion_mongo import ConexionMongo

if __name__ == "__main__":
    # Conectar a MongoDB
    conexion = ConexionMongo()
    db = conexion.get_db()

    # Crear grupos
    grupos = [
        Grupo(100, "Clientes", ["Ver-Productos", "Agregar-Carrito", "Ver-Carrito", "Eliminar-Carrito", "Realizar-Pedido", "Ver-Pedido", "Cancelar-Pedido"]),
        Grupo(200, "Administrador-Productos", ["Agregar-Producto", "Editar-Producto", "Eliminar-Producto", "Ver-Productos"]),
        Grupo(300, "Administrador-Pedidos", ["Ver-Pedidos", "Procesar-Pedido", "Cancelar-Pedido", "Ver-Detalle-Pedido"]),
        Grupo(400, "Soporte-Cliente", ["Ver-Clientes", "Ver-Pedidos", "Gestionar-Reclamos"])
    ]

    # Insertar grupos en la base de datos
    for grupo in grupos:
        db.grupos.insert_one(vars(grupo))

    print("Grupos subidos a la base de datos.")
