# main.py
import database
from gui import Application

def main():
    # 1. Inicializar la Base de Datos SQLite
    database.inicializar_bd()
    
    # 2. Arrancar la Interfaz Gráfica de Usuario (Tkinter)
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()
