# Proyecto de Ejemplo para el Curso de Deployments

Este proyecto es una aplicación web de ejemplo desarrollada para el curso de *Deployments* en Platzi. Su propósito es brindar una experiencia práctica sobre cómo implementar una aplicación web en un servidor de producción. Aquí, los estudiantes aprenderán a configurar, desplegar y gestionar aplicaciones en un entorno de producción utilizando las herramientas y configuraciones más comunes.

## Requisitos Previos

- **Python 3.7+**: Asegúrate de tener instalada una versión compatible de Python.
- **Virtualenv**: Es recomendable trabajar en un entorno virtual para aislar las dependencias del proyecto.
- **Git**: Para clonar el repositorio.

## Configuración del Proyecto Localmente

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/luismartinez/django-basics.git
   ```

2. **Crear un entorno virtual y activarlo** (opcional pero recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**:

   ```bash
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo**:

   ```bash
   python manage.py runserver
   ```

   La aplicación estará disponible en `http://127.0.0.1:8000/`.

## Variables de Entorno

Configura las variables de entorno en un archivo `.env` en la raíz del proyecto. Este archivo está incluido en `.gitignore` para evitar su inclusión en el repositorio y proteger datos sensibles.

Lista de variables importantes para configurar:

- **`SECRET_KEY`**: Clave secreta utilizada para encriptar datos sensibles. Genera una clave segura y única para cada entorno.
- **`DEBUG`**: Activa el modo de depuración (solo para entornos de desarrollo). Valor recomendado en producción: `False`.
- **`ALLOWED_HOSTS`**: Lista de hosts permitidos para el sitio. Por defecto incluye `0.0.0.0` y `deploywithpython.local`.
- **`DATABASE_URL`**: URL de conexión a la base de datos en formato de cadena de conexión. El valor predeterminado es `sqlite:///db.sqlite3`.

## Ejemplo de Configuración `.env`

```dotenv
SECRET_KEY='tu_clave_secreta_aqui'
DEBUG=True
ALLOWED_HOSTS='0.0.0.0, deploywithpython.local'
DATABASE_URL='sqlite:///db.sqlite3'
```


## Calculator

El proyecto incluye una aplicación de ejemplo llamada **Calculator** que se puede acceder en `http://127.0.0.1:8000/calculator/`. Esta aplicación es una calculadora de división y permite a los estudiantes realizar cálculos de división con dos números.

La url `/calculator/divide/` recibe dos parámetros: `x` y `y`, que representan los numeradores y denominadores, respectivamente. El resultado de la división se muestra en la pantalla de resultado.

## Despliegue en Producción

Para desplegar la aplicación en producción, asegúrate de ajustar las variables de entorno correspondientes, especialmente `DEBUG=False`, y configura un servidor de bases de datos adecuado.

Para más detalles sobre el despliegue, consulta la documentación del curso.

