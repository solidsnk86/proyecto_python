<div align="center">
 |----------| | SENSE_IA | 
</div>

# Proyecto Python con IA y login de usuarios

Este proyecto combina una aplicación de chat con IA y un sistema de login de usuarios utilizando PostgreSQL como base de datos.

## Características

- **Chat con IA**: Los usuarios pueden interactuar con un asistente de IA desde la terminal para obtener respuestas a sus preguntas y solicitudes.
- **Autenticación de usuarios**: Los usuarios pueden registrarse, iniciar sesión y cerrar sesión desde la terminal.
- **Gestión de usuarios**: Los administradores pueden ver, editar y eliminar cuentas de usuario.
- **Base de datos PostgreSQL**: Todos los datos de usuarios y conversaciones se almacenan en una base de datos PostgreSQL.

## Tecnologías utilizadas

- **Python**: Lenguaje de programación utilizado para desarrollar la aplicación.
- **pycog2**: Biblioteca de Python utilizada para interactuar con la base de datos PostgreSQL.
- **PostgreSQL**: Sistema de gestión de base de datos relacional utilizado para almacenar datos de usuarios y conversaciones.

## Configuración del proyecto

Clona el repositorio del proyecto:

```bash
git clone https://github.com/tu-usuario/sense-ia.git
```

Crea un entorno virtual e instala las dependencias:

```bash
cd sense-ia
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Configura las variables de entorno:

```bash
cp .env.example .env
```

Edita el archivo `.env` y proporciona los datos de conexión de tu base de datos PostgreSQL creada en pgAdmin.

Ejecuta la aplicación:

```bash
python main.py
```

### Uso de la aplicación

Registro de usuario
Ejecuta la aplicación y selecciona la opción "👉 Crear usuario" desde el menú principal.

Ingresa la información solicitada. El sistema guardará el nuevo usuario en la base de datos.

Inicio de sesión
Selecciona la opción "🔐 Iniciar sesión" desde el menú principal.

Ingresa tu correo usuario y contraseña.

Si los datos son correctos, accederás al sistema.

Chat con IA
Una vez iniciada la sesión, Se ingresa al "Chat con Sense_IA".

Escribe tus mensajes directamente en la terminal.

El asistente de IA responderá por texto en la misma interfaz.

### Contribución

Haz un fork del repositorio.

Crea una nueva rama para tu funcionalidad o corrección de errores.
Realiza los cambios necesarios y asegúrate de que todo funciona correctamente.
Envía una pull request con una descripción detallada de tus cambios.
¡Gracias por tu interés en este proyecto!