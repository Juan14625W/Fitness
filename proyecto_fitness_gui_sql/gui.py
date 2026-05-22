# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from auth import SistemaAutenticacion
from calculator import CalculadoraFitness

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Fitness Inteligente")
        self.geometry("680x550")
        self.resizable(False, False)
        
        # Configurar paleta de colores y estilos visuales limpios (Flat / Modern)
        self.bg_color = "#F4F6F7"      # Gris claro de fondo
        self.primary_color = "#2C3E50" # Azul marino oscuro elegante
        self.accent_color = "#1ABC9C"  # Turquesa brillante para realces
        self.text_color = "#34495E"    # Texto oscuro
        
        self.configure(bg=self.bg_color)
        
        # Configurar Estilos de TTK
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('.', background=self.bg_color, foreground=self.text_color)
        self.style.configure('TLabel', font=('Helvetica', 10), background=self.bg_color)
        self.style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'), foreground=self.primary_color, background=self.bg_color)
        self.style.configure('Sub.TLabel', font=('Helvetica', 11, 'italic'), foreground="#7F8C8D", background=self.bg_color)
        
        # Estilos para Notebook (Pestañas de la calculadora)
        self.style.configure('TNotebook', background=self.bg_color, borderwidth=0)
        self.style.configure('TNotebook.Tab', font=('Helvetica', 10, 'bold'), padding=[10, 5], background="#BDC3C7")
        self.style.map('TNotebook.Tab', background=[('selected', self.accent_color)], foreground=[('selected', 'white')])

        # Contenedor principal de pantallas
        self.container = tk.Frame(self, bg=self.bg_color)
        self.container.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        
        self.usuario_activo = None
        self.mostrar_pantalla_principal()

    def limpiar_contenedor(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def mostrar_pantalla_principal(self):
        self.limpiar_contenedor()
        
        # Banner Superior Estilizado
        banner = tk.Frame(self.container, bg=self.primary_color, height=80)
        banner.pack(fill="x", pady=(15, 25))
        lbl_title = tk.Label(banner, text="BIENVENIDO AL RETO FITNESS", font=("Helvetica", 18, "bold"), fg="white", bg=self.primary_color)
        lbl_title.pack(pady=20)
        
        lbl_sub = ttk.Label(self.container, text="Gestione sus métricas corporales", style="Sub.TLabel")
        lbl_sub.pack(pady=(0, 30))

        # Marco de Botones
        btn_frame = tk.Frame(self.container, bg=self.bg_color)
        btn_frame.pack(pady=10)

        # Configuración común de botones estilizados planos
        btn_opts = {"font": ("Helvetica", 11, "bold"), "fg": "white", "bd": 0, "activebackground": "#34495E", "cursor": "hand2", "width": 28, "pady": 10}

        btn_reg = tk.Button(btn_frame, text="Registrar Nuevo Usuario", bg=self.accent_color, command=self.mostrar_registro, **btn_opts)
        btn_reg.pack(pady=10)

        btn_log = tk.Button(btn_frame, text="Iniciar Sesión", bg="#3498DB", command=self.mostrar_login, **btn_opts)
        btn_log.pack(pady=10)

        btn_db = tk.Button(btn_frame, text="Ver Base de Datos", bg="#9B59B6", command=self.mostrar_persistencia, **btn_opts)
        btn_db.pack(pady=10)

        btn_salir = tk.Button(btn_frame, text="Salir del Sistema", bg="#E74C3C", command=self.quit, **btn_opts)
        btn_salir.pack(pady=10)

    def mostrar_registro(self):
        self.limpiar_contenedor()

        ttk.Label(self.container, text="REGISTRO DE NUEVO DEPORTISTA", style="Header.TLabel").pack(pady=(15, 20))

        form_frame = tk.Frame(self.container, bg=self.bg_color)
        form_frame.pack(pady=5)

        fields = [
            ("Nombre Completo:", "nombre"),
            ("Cédula o Identificación:", "cedula"),
            ("Fecha Nacimiento (DD/MM/AAAA):", "fecha_nac"),
            ("Altura en centímetros (cm):", "altura"),
            ("Peso en Kilogramos (kg):", "peso")
        ]

        self.entradas_registro = {}
        for idx, (label_text, key) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=idx, column=0, sticky="w", pady=6, padx=10)
            entry = ttk.Entry(form_frame, font=("Helvetica", 10), width=30)
            entry.grid(row=idx, column=1, pady=6, padx=10)
            self.entradas_registro[key] = entry

        # Campo Género
        ttk.Label(form_frame, text="Género Biológico:").grid(row=len(fields), column=0, sticky="w", pady=6, padx=10)
        self.combo_genero = ttk.Combobox(form_frame, values=["Hombre", "Mujer"], state="readonly", font=("Helvetica", 10), width=28)
        self.combo_genero.grid(row=len(fields), column=1, pady=6, padx=10)
        self.combo_genero.current(0)

        # Botones de acción
        btn_frame = tk.Frame(self.container, bg=self.bg_color)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Guardar y Crear Clave", bg=self.accent_color, fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=15, pady=8, command=self.procesar_registro).pack(side="left", padx=15)
        tk.Button(btn_frame, text="Volver al Menú", bg="#7F8C8D", fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=15, pady=8, command=self.mostrar_pantalla_principal).pack(side="left", padx=15)

    def procesar_registro(self):
        nombre = self.entradas_registro["nombre"].get().strip()
        cedula = self.entradas_registro["cedula"].get().strip()
        fecha_nac = self.entradas_registro["fecha_nac"].get().strip()
        altura = self.entradas_registro["altura"].get().strip()
        peso = self.entradas_registro["peso"].get().strip()
        genero = self.combo_genero.get()

        if not (nombre and cedula and fecha_nac and altura and peso):
            messagebox.showerror("Error", "Todos los campos son totalmente obligatorios.")
            return

        try:
            float(altura)
            float(peso)
        except ValueError:
            messagebox.showerror("Error", "La altura y el peso deben ser valores numéricos válidos.")
            return

        clave = SistemaAutenticacion.registrar_usuario(nombre, cedula, fecha_nac, altura, peso, genero)
        
        if clave:
            messagebox.showinfo("Registro Exitoso", f"Usuario guardado en la BD con éxito.\n\nSu clave autogenerada es:\n👉 {clave} 👈\n\nUse esta clave y su cédula para ingresar a la calculadora.")
            self.mostrar_pantalla_principal()
        else:
            messagebox.showerror("Error", "No se pudo registrar. Es posible que esa cédula ya se encuentre registrada en el sistema SQL.")

    def mostrar_login(self):
        self.limpiar_contenedor()

        ttk.Label(self.container, text="INICIAR SESIÓN", style="Header.TLabel").pack(pady=(30, 20))

        login_frame = tk.Frame(self.container, bg=self.bg_color)
        login_frame.pack(pady=10)

        ttk.Label(login_frame, text="Número de Cédula:").grid(row=0, column=0, sticky="w", pady=8, padx=10)
        self.ent_login_cedula = ttk.Entry(login_frame, font=("Helvetica", 11), width=25)
        self.ent_login_cedula.grid(row=0, column=1, pady=8, padx=10)

        ttk.Label(login_frame, text="Contraseña Generada:").grid(row=1, column=0, sticky="w", pady=8, padx=10)
        self.ent_login_clave = ttk.Entry(login_frame, font=("Helvetica", 11), width=25, show="*")
        self.ent_login_clave.grid(row=1, column=1, pady=8, padx=10)

        btn_frame = tk.Frame(self.container, bg=self.bg_color)
        btn_frame.pack(pady=25)

        tk.Button(btn_frame, text="Ingresar", bg="#3498DB", fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=20, pady=8, command=self.procesar_login).pack(side="left", padx=15)
        tk.Button(btn_frame, text="Cancelar", bg="#7F8C8D", fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=20, pady=8, command=self.mostrar_pantalla_principal).pack(side="left", padx=15)

    def procesar_login(self):
        cedula = self.ent_login_cedula.get().strip()
        clave = self.ent_login_clave.get().strip()

        usuario = SistemaAutenticacion.validar_acceso(cedula, clave)
        if usuario:
            self.usuario_activo = usuario
            self.mostrar_calculadora()
        else:
            messagebox.showerror("Acceso Denegado", "La cédula y la contraseña no coinciden con ningún deportista en nuestra base de datos SQL.")

    def mostrar_calculadora(self):
        self.limpiar_contenedor()

        # Encabezado con datos del usuario activo
        header_frame = tk.Frame(self.container, bg=self.primary_color, padx=15, pady=10)
        header_frame.pack(fill="x", pady=(10, 15))
        
        lbl_usr = tk.Label(header_frame, text=f"Atleta: {self.usuario_activo.nombre_completo} | Edad: {self.usuario_activo.edad} años", font=("Helvetica", 11, "bold"), fg="white", bg=self.primary_color)
        lbl_usr.pack(side="left")
        
        btn_logout = tk.Button(header_frame, text="Cerrar Sesión", bg="#E74C3C", fg="white", bd=0, font=("Helvetica", 9, "bold"), padx=10, command=self.mostrar_pantalla_principal)
        btn_logout.pack(side="right")

        # Widget de Pestañas (Notebook)
        notebook = ttk.Notebook(self.container)
        notebook.pack(fill="both", expand=True, pady=5)

        # 1. PESTAÑA PESO IDEAL
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Peso Ideal (IBW)")
        ibw = CalculadoraFitness.calcular_peso_ideal(self.usuario_activo)
        txt_ibw = f"Según la fórmula del Dr. Miller,\nsu peso ideal sugerido es de:\n\n👉 {ibw:.2f} Kg 👈"
        tk.Label(tab1, text=txt_ibw, font=("Helvetica", 13, "bold"), fg=self.primary_color, justify="center").pack(pady=40)

        # 2. PESTAÑA CALORÍAS QUEMADAS
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Quemar Calorías")
        
        lbl_info = ttk.Label(tab2, text="Calcule el gasto energético según la actividad física:")
        lbl_info.pack(pady=(15, 10))
        
        calc_form = tk.Frame(tab2)
        calc_form.pack(pady=5)
        
        ttk.Label(calc_form, text="Seleccione Actividad (MET):").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.combo_met = ttk.Combobox(calc_form, values=["Caminar (MET: 2)", "Tenis (MET: 5)", "Correr (MET: 6)", "Nadar (MET: 9.8)", "Bicicleta (MET: 14)"], state="readonly", width=22)
        self.combo_met.grid(row=0, column=1, pady=5, padx=5)
        self.combo_met.current(0)
        
        ttk.Label(calc_form, text="Tiempo de Actividad (minutos):").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.ent_tiempo = ttk.Entry(calc_form, width=24)
        self.ent_tiempo.grid(row=1, column=1, pady=5, padx=5)
        
        self.lbl_res_calorias = tk.Label(tab2, text="", font=("Helvetica", 12, "bold"), fg="#27AE60")
        self.lbl_res_calorias.pack(pady=15)
        
        tk.Button(tab2, text="Calcular Gasto Energético", bg=self.accent_color, fg="white", bd=0, font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.calcular_calorias).pack()

        # 3. PESTAÑA GRASA CORPORAL E IMC
        tab3 = ttk.Frame(notebook)
        notebook.add(tab3, text="Porcentaje de Grasa & IMC")
        imc = CalculadoraFitness.calcular_imc(self.usuario_activo.peso_kg, self.usuario_activo.altura_cm)
        grasa = CalculadoraFitness.calcular_porcentaje_grasa(self.usuario_activo)
        
        txt_grasa = f"Índice de Masa Corporal (IMC): {imc:.2f}\n\nPorcentaje de Grasa Corporal Estimado: {grasa:.2f}%"
        tk.Label(tab3, text=txt_grasa, font=("Helvetica", 13, "bold"), fg=self.primary_color, justify="center").pack(pady=40)

        # 4. PESTAÑA TASA METABÓLICA BASAL
        tab4 = ttk.Frame(notebook)
        notebook.add(tab4, text="Índice Metabólico (TMB)")
        tmb = CalculadoraFitness.calcular_tmb(self.usuario_activo)
        txt_tmb = f"Su Tasa Metabólica Basal (TMB) es de:\n\n👉 {tmb:.2f} kcal/día 👈\n\nRepresenta las calorías mínimas que su cuerpo necesita para sobrevivir."
        tk.Label(tab4, text=txt_tmb, font=("Helvetica", 13, "bold"), fg=self.primary_color, justify="center").pack(pady=40)

    def calcular_calorias(self):
        actividades_met = [2, 5, 6, 9.8, 14]
        idx = self.combo_met.current()
        met = actividades_met[idx]
        
        tiempo_str = self.ent_tiempo.get().strip()
        if not tiempo_str:
            messagebox.showerror("Error", "Ingrese la duración en minutos.")
            return
        try:
            tiempo = float(tiempo_str)
        except ValueError:
            messagebox.showerror("Error", "El tiempo debe ser un número válido.")
            return
            
        calorias = CalculadoraFitness.calcular_calorias_quemadas(self.usuario_activo.peso_kg, tiempo, met)
        self.lbl_res_calorias.config(text=f"🔥 ¡Has quemado aproximadamente {calorias:.2f} kcal! 🔥")

    def mostrar_persistencia(self):
        self.limpiar_contenedor()

        ttk.Label(self.container, text="PERSISTENCIA: USUARIOS REGISTRADOS EN SQL", style="Header.TLabel").pack(pady=(15, 15))

        # Crear una tabla Treeview bonita
        tabla_frame = tk.Frame(self.container)
        tabla_frame.pack(fill="both", expand=True, pady=5)

        columnas = ("nombre", "cedula", "contrasena")
        self.tree = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=12)
        
        self.tree.heading("nombre", text="Nombre Completo Atleta")
        self.tree.heading("cedula", text="Cédula / ID")
        self.tree.heading("contrasena", text="Contraseña Asignada")
        
        self.tree.column("nombre", width=250, anchor="w")
        self.tree.column("cedula", width=150, anchor="center")
        self.tree.column("contrasena", width=180, anchor="center")

        # Agregar Scrollbar a la tabla
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Cargar datos reales desde la BD SQL
        lista_usuarios = SistemaAutenticacion.obtain_todos() if hasattr(SistemaAutenticacion, "obtain_todos") else SistemaAutenticacion.obtener_todos()
        for u in lista_usuarios:
            self.tree.insert("", "end", values=u)

        tk.Button(self.container, text="Volver al Menú", bg="#7F8C8D", fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=20, pady=8, command=self.mostrar_pantalla_principal).pack(pady=15)
