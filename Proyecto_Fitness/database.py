# database.py
import sqlite3

def inicializar_bd():
    """Crea la base de datos SQL y la tabla de usuarios si no existe."""
    conn = sqlite3.connect("fitness_poo.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            cedula TEXT PRIMARY KEY,
            nombre_completo TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            altura_cm REAL NOT NULL,
            peso_kg REAL NOT NULL,
            genero TEXT NOT NULL,
            contrasena TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def registrar_usuario_bd(cedula, nombre, fecha_nac, altura, peso, genero, contrasena):
    """Inserta un nuevo registro de usuario en la base de datos SQL."""
    try:
        conn = sqlite3.connect("fitness_poo.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (cedula, nombre_completo, fecha_nacimiento, altura_cm, peso_kg, genero, contrasena)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (cedula, nombre, fecha_nac, altura, peso, genero, contrasena))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Cédula ya existe

def obtener_usuario_bd(cedula):
    """Busca un usuario por su cédula para autenticación y carga de datos."""
    conn = sqlite3.connect("fitness_poo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE cedula = ?", (cedula,))
    row = cursor.fetchone()
    conn.close()
    return row

def obtener_todos_usuarios_bd():
    """Recupera los usuarios guardados para el módulo de Persistencia."""
    conn = sqlite3.connect("fitness_poo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_completo, cedula, contrasena FROM usuarios")
    rows = cursor.fetchall()
    conn.close()
    return rows
