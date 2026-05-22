# Proyecto Fitness

**Calculadora Fitness Modular Avanzada**

Este proyecto es una aplicación de escritorio en Python que ayuda a atletas y personas activas a registrar sus datos personales, iniciar sesión de forma segura y obtener indicadores de salud importantes.

## ¿Qué hace esta aplicación?

- Permite registrar nuevos usuarios con: nombre completo, cédula, fecha de nacimiento, altura, peso y género.
- Genera automáticamente una contraseña segura basada en el nombre y la cédula.
- Al iniciar sesión, muestra una calculadora de métricas físicas y de salud.
- Calcula:
  - Peso ideal según la fórmula del Dr. Miller.
  - Calorías quemadas según actividad física y tiempo.
  - Índice de Masa Corporal (IMC).
  - Porcentaje de grasa corporal estimado.
  - Tasa Metabólica Basal (TMB).
- Guarda los usuarios en una base de datos SQLite local llamada `fitness_poo.db`.
- Muestra una tabla con los usuarios registrados y sus credenciales.

## Arquitectura general

La aplicación está organizada en módulos claros y separados para que el código sea más mantenible.

### `main.py`
- Punto de entrada del proyecto.
- Inicializa la base de datos y arranca la interfaz gráfica.

### `database.py`
- Maneja la conexión con SQLite.
- Crea la tabla `usuarios` si no existe.
- Inserta y lee usuarios de la base de datos.

### `models.py`
- Define la clase `Usuario`.
- Convierte datos de entrada en valores numéricos.
- Genera la contraseña automática del usuario.
- Calcula la edad a partir de la fecha de nacimiento.

### `auth.py`
- Controla el registro y la autenticación de usuarios.
- Envía datos a la base de datos y reconstruye el objeto `Usuario` al iniciar sesión.

### `calculator.py`
- Contiene todos los algoritmos de cálculo de salud.
- Separa la lógica matemática de la interfaz.

### `gui.py`
- Define la aplicación visual usando Tkinter y ttk.
- Crea las pantallas de registro, login, resultados y persistencia.
- Gestiona la interacción del usuario y muestra mensajes claros.

## Flujo de uso

1. Ejecuta `main.py` con Python.
2. Registra un nuevo deportista desde la pantalla principal.
3. Copia la clave generada automáticamente.
4. Inicia sesión con tu cédula y la clave.
5. Navega por las pestañas para ver las métricas de salud.
6. Consulta la tabla de usuarios registrados en la base de datos.

## Cómo ejecutar

Desde el directorio del proyecto:

```bash
python main.py
```

> Asegúrate de tener Python 3 instalado y que Tkinter esté disponible en tu sistema.

## Formatos y reglas de datos

- Fecha de nacimiento: `DD/MM/AAAA`
- Altura: centímetros (`cm`)
- Peso: kilogramos (`kg`)
- Género: `Hombre` o `Mujer`
- La contraseña se forma así:
  - Primeras dos letras del primer nombre
  - Primeras dos letras del primer apellido
  - Cédula completa

## Estructura de archivos

- `main.py` — arranque de la aplicación.
- `database.py` — gestión de SQLite.
- `models.py` — modelo `Usuario` y cálculo de edad.
- `auth.py` — registro, login y manejo de credenciales.
- `calculator.py` — fórmulas de salud.
- `gui.py` — interfaz gráfica y navegación.
- `README.txt` — descripción breve existente.

## Detalle de los cálculos

- `Peso ideal`: usa la fórmula del Dr. Miller.
- `Calorías quemadas`: cálculo con MET y tiempo de actividad.
- `IMC`: peso dividido por altura al cuadrado.
- `% Grasa corporal`: basado en IMC, edad y género.
- `TMB`: tasa metabólica basal según sexo, peso, edad y altura.

## Qué puedes mejorar a futuro

- Guardar contraseñas de forma segura con hashing.
- Validar fechas más estrictamente.
- Añadir más actividades y valores MET personalizados.
- Ofrecer gráficos y reportes de progreso.
- Incluir exportación a CSV o PDF.

## Notas finales

Este proyecto busca ser una herramienta simple y práctica para seguir métricas de fitness de forma rápida. La separación en capas (`gui`, `auth`, `models`, `calculator` y `database`) facilita entender el proyecto y escalarlo cuando quieras agregar nuevas funciones.
