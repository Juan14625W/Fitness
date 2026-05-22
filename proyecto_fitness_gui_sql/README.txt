PROYECTO: CALCULADORA FITNESS MODULAR AVANZADA
===================================================
Características agregadas:
1. Base de datos SQL (SQLite integrado, crea automáticamente el archivo 'fitness_poo.db').
2. Interfaz Gráfica de Usuario (GUI) moderna, limpia y responsive usando Tkinter y TTK.
3. Arquitectura limpia POO con capas modulares separadas.

Estructura de Archivos:
- main.py        : Punto de arranque principal de la app.
- database.py    : Control lógico de sentencias y transacciones SQL.
- models.py      : Definición de la entidad Usuario (POO), encapsulamiento y cálculo de la edad.
- calculator.py  : Algoritmos matemáticos y métricas de salud (Dr. Miller, MET, IMC, TMB).
- auth.py        : Puente de validación y autenticación entre GUI, modelos y SQL.
- gui.py         : Diseño visual de la ventana, formularios, tablas de persistencia y pestañas (Notebook).

Cómo ejecutar el proyecto:
Abra la terminal en el directorio raíz descomprimido del proyecto y ejecute:
python main.py
