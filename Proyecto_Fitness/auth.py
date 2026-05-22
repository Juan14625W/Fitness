# auth.py
import database
from models import Usuario

class SistemaAutenticacion:
    
    @staticmethod
    def registrar_usuario(nombre, cedula, fecha_nac, altura, peso, genero):
        """Registra un usuario instanciando el objeto POO y enviándolo a SQL."""
        # Crear la instancia del objeto POO
        usuario = Usuario(nombre, cedula, fecha_nac, altura, peso, genero)
        
        # Guardar en base de datos SQL
        exito = database.registrar_usuario_bd(
            usuario.cedula,
            usuario.nombre_completo,
            usuario.fecha_nacimiento,
            usuario.altura_cm,
            usuario.peso_kg,
            usuario.genero,
            usuario.contrasena
        )
        if exito:
            return usuario.contrasena
        return None

    @staticmethod
    def validar_acceso(cedula, contrasena):
        """Valida credenciales en la base de datos SQL y mapea a Objeto POO."""
        row = database.obtener_usuario_bd(cedula)
        if row and row[6] == contrasena:
            # Re-construye el objeto Usuario desde la fila SQL recuperada
            # row: (cedula, nombre_completo, fecha_nacimiento, altura_cm, peso_kg, genero, contrasena)
            return Usuario(row[1], row[0], row[2], row[3], row[4], row[5], row[6])
        return None

    @staticmethod
    def obtener_todos():
        """Módulo de persistencia pura desde SQL."""
        return database.obtener_todos_usuarios_bd()
