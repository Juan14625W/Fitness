# models.py
from datetime import datetime

class Usuario:
    def __init__(self, nombre_completo, cedula, fecha_nacimiento, altura_cm, peso_kg, genero, contrasena=None):
        """
        Clase del Modelo de Usuario (POO).
        :param fecha_nacimiento: String en formato 'DD/MM/AAAA'
        """
        self.nombre_completo = nombre_completo
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.altura_cm = float(altura_cm)
        self.peso_kg = float(peso_kg)
        self.genero = genero.lower()
        self.contrasena = contrasena if contrasena else self._generar_clave()

    def _generar_clave(self):
        """Genera la clave según reglas del reto fitness."""
        partes = self.nombre_completo.split()
        primer_nombre = partes[0] if len(partes) > 0 else "xx"
        primer_apellido = partes[1] if len(partes) > 1 else "xx"
        
        letra_nombre = primer_nombre[:2].lower()
        letra_apellido = primer_apellido[:2].lower()
        
        return f"{letra_nombre}{letra_apellido}{self.cedula}"

    @property
    def edad(self):
        """Calcula la edad dinámica a partir de la fecha de nacimiento."""
        try:
            fecha_nac = datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y")
            hoy = datetime.today()
            return hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        except ValueError:
            return 25  # Valor por defecto si hay un error de parseo externo
