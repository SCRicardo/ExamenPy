from pymongo import MongoClient

class ConexionMongo:
    def __init__(self):
        # URI de conexión a MongoDB
        self.uri = "mongodb+srv://equipo1:admin123@usuarios.8hicz.mongodb.net/usuarios?retryWrites=true&w=majority&appName=usuarios"
        self.client = MongoClient(self.uri)
        self.db = self.client['usuarios']  # Asegúrate de que 'usuarios' es el nombre correcto de la base de datos

    def get_db(self):
        return self.db
