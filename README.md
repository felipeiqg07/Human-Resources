Requerimientos:
Ejecutar pip install -r requirements.txt

En caso de  que no funcione el txt estos son los requerimientos:
Oracledb (configurar base de datos local tambien)
Django
Ambiente virtual de python (en caso de tener windows)
Djangorestframework

Como ejecutar la Base de Datos, dentro de los ajustes de galaxymusic/galaxymusic/settings
Se debe cambiar la configuración de la Base de datos e ingresar la localización de la wallet extraida, en este caso la carpeta admin de la entrega, la contraseña ya se encuentra ingresada.
Alternativamente en caso de no lograr hacer funcionar la wallet se pueden ingresar los datos de una BDD local de Oracle.

Nota:
Quedó una app de poll de sobra por andar haciendo documentación,
podría servir en caso de tener plazo de sobra y necesitar mas funciones.

Como hacer funcionar POSTMAN:
Iniciar el servidor y asegurarse de que todo de la app funciona bién
Asegurarse de que se realizaron las migraciones a la BDD local
Instalar la app de POSTMAN de escritorio
Ingresar a la lista de Empleados u otra api
Seleccionar GET como json
Copiar URL de la pagina con los json
En un nuevo archivo de POSTMAN ingresar la url del json del proyecto
