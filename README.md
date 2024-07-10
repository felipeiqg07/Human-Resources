Paso a paso de como ejecutar programa:
1. Crear VENV:
  Abrir terminal en Directorio principal de Galaxymusic (no confundir con galaxymusic/galaxymusic directorio de ajustes)
  python -m venv venv
2. Instalar requerimientos txt
  luego de crear el venv se debe ejecutar el venv con venv\Scripts\activate, o source venv\bin\activate (slashes pueden variar segun OS)
3. Ejecutar comando de runserver
  En el directorio principal ejecutar: python manage.py runserver

A continuación se ejecutará el programa dentro del localhost
Para probar el Endpoint creado por HR que permite a los programas de departamentos consumir la API se debe realizar una solicitud de POST al endpoint de http://127.0.0.1:8000/api/api-token-auth/,
en caso de usar POSTMAN se debe enviar los siguientes parametros:
  Body: Username admin
        Password admin
  Header: X-CSRFToken (token)
  En caso de no contar con un csrf token este se debe extraer a traves de un GET al mismo endpoint, luego de enviar el GET en el apartado de cookies se encontrará el token de csrf

Actualmente el programa solo cuenta con un CRUD basico de empleados, un Login y el Endpoint mencionado anteriormente
