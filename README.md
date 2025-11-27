### README – Backend Urbanización
1. Descripción del proyecto

Backend Urbanización es un sistema de gestión y control de acceso para una urbanización.
El backend permite administrar:

-Viviendas
-Residentes
-Vehículos
-Visitantes
-Guardias
-Invitaciones
-Registros de acceso

2. Tecnologías utilizadas
Tecnología	Descripción
Python 3.x	Lenguaje principal
Django 5.x	Framework backend
Django REST Framework	API REST
PostgreSQL	Base de datos
SimpleJWT	Autenticación por tokens
python-dotenv	Gestión de variables de entorno

3. Requisitos previos

-Asegúrese de tener instalado:
-Python 3.10 o superior
-PostgreSQL 14 o superior
-Git
-Postman

4. Instalación del proyecto
4.1. Clonar el repositorio (si aplica)
git clone https://github.com/tu-usuario/backend-urbanizacion.git
cd backend-urbanizacion

4.2. Crear entorno virtual
python -m venv .venv

Activar:
Windows:
.venv\Scripts\activate

Linux/Mac:
source .venv/bin/activate

4.3. Instalar dependencias
pip install -r requirements.txt

5. Configuración de variables de entorno (.env)

Crear un archivo .env en la raíz del proyecto:

SECRET_KEY=super-secret-key
DEBUG=True
ALLOWED_HOSTS=*

DB_NAME=urbanizaciondb
DB_USER=postgres
DB_PASS=postgres
DB_HOST=localhost
DB_PORT=5432

JWT_ACCESS_MINUTES=60
JWT_REFRESH_DAYS=7

6. Configuración de PostgreSQL

Crear la base de datos:
CREATE DATABASE urbanizaciondb;

Si desea crear un usuario:

CREATE USER urbanizacion_user WITH PASSWORD '12345';
GRANT ALL PRIVILEGES ON DATABASE urbanizaciondb TO urbanizacion_user;

7. Migraciones
- Ejecutar migraciones:
python manage.py makemigrations
python manage.py migrate

- Crear superusuario:
python manage.py createsuperuser

8. Ejecutar el servidor
python manage.py runserver

El backend estará disponible en:
- http://127.0.0.1:8000/api/

9. Autenticación (JWT)
9.1. Obtener Token
POST /api/login/

Body:

{
  "username": "admin",
  "password": "123456"
}

Respuesta:

{
  "refresh": "xxxxx",
  "access": "yyyyy"
}

9.2. Refresh Token
POST /api/refresh/

10. Permisos y roles

El sistema implementa roles básicos:

Acción	Invitado	Usuario normal	Admin
GET	      SI              SI        SI
POST	    NO              SI        SI
PUT	      NO              NO        SI
DELETE	  NO              NO        SI

Permisos implementados mediante BasicRolePermission.

11. Endpoints principales

Base URL:
- /api/

* Viviendas

GET /api/viviendas/

POST /api/viviendas/

GET /api/viviendas/<id>/

PUT /api/viviendas/<id>/

DELETE /api/viviendas/<id>/

* Residentes

GET /api/residentes/

POST /api/residentes/

GET /api/residentes/<id>/

PUT /api/residentes/<id>/

DELETE /api/residentes/<id>/

* Vehículos

GET /api/vehiculos/

POST /api/vehiculos/

GET /api/vehiculos/<id>/

PUT /api/vehiculos/<id>/

DELETE /api/vehiculos/<id>/

* Visitantes
* Guardias
* Invitaciones
* Registros de acceso


12. Ejemplo de una petición protegida con token
Crear vivienda -> Posee token

POST /api/viviendas/

Headers:

Authorization: Bearer <ACCESS_TOKEN>
Content-Type: application/json


Body:

{
  "numero": "25B",
  "calle": "Los Nogales",
  "propietario": "Ana Pérez"
}

13. Manejo de errores

Los errores son devueltos con formato consistente:

{
  "detail": "Not found.",
  "status_code": 404,
  "error_type": "NotFound"
}

14. Paginación

Todas las listas utilizan paginación automática:

{
  "count": 50,
  "next": "...",
  "previous": null,
  "results": [ ... ]
}

15. Colección Postman

Se incluye una colección Postman con:

- Login JWT
- Refresh Token
- Endpoints CRUD
- Pruebas de permisos y roles
- Ejemplos de uso


16. Autor

Joselyn Saavedra
Proyecto académico – Backend Urbanización
2025
