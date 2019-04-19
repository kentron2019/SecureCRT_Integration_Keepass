# SecureCRT Integration Keepass

Conectarse a keepass para obtener el usuario y contarseña desde SecureCRT.
El Objetivo es tener todos los usurios y contraseñas guardadas en KeePass.

Este desarollo en una versión inicial para poder utilizarlo desde SecureCRT con el plugin 
ya desarollado por Perry Nguyen que permite hacelro con el navegador Chrome y Firefox. 

¿Cómo funciona?
--------------

En la sessión de SecureCRT cargamos el fichero .vbs proporcionado y en el campo de argumento ponemos la IP que queremos conectarnos.
Este campo de Argumento con la IP se usa para consultar en KeePass y obtener el usuario y contraseña.
Previamente en Keepass hay que guardar el usuario, la contraseña y en el campo de URL: la IP.

El script vbs se encargará de ejecutar el script python Generic_Conector.py que sirve para consultar si existe un registro con la IP
proporcionada y devolvernos el usuario y contraseña.

En el SecureCRT habrá que gaurdar todas las credenciales referenciándolas o  guardándolas por su IP en el campo URL.

¿Cómo empezar?
--------------
Creamos una carpeta por ejemplo en:
C:\Users\[usuario_windows]\AppData\Roaming\VanDyke\k-script\SecureCRT_Integration_Keepass

Dentro de la carpeta copiamos ambos fichero:
- SecureCRT_Keepass.vbs
- Generic_Conector.py

En la opción propiedad de sessión SecureCRT se carga el fichero: SecureCRT_Keepass.vbs
* Habrá que modificar el path donde se guardo el fichero Generic_Conector.py

Importante:
* Esta modificación se tiene que hacer en el fichero: SecureCRT_Keepass.vbs

Pre requisitos
--------------

El fichero Generic_Conector.py necesita tener instalada la librería:

https://github.com/pfn/keepasshttp.git

pip install keepasshttp

* Importante seguir el manual de instalación explicado por Perry Nguyen.

Ee las opciones de SecureCRT en propiedad de la sesión dentro de "connection" -> "Logon Actions" la opción:
- Display logo prompts in terminal windows

Tiene que estar activado.


Versiones
---------

Este desarollo ha sido probado en el entorno: 

- SecureCRT (Versión: 8.5.3)
- Chrome (Versión: 73.0.3683.103 (Build oficial) (64 bits))
- Python (Versión: Python 2.7.12)
- Probado también con Python (Versión: Python 3.6.4)
- KeePass Password Safe (Versión: 2.40)
- KeePAss Plugin: KeePassHttp (Versión: 1.8.4.2)


Autor:
------
Karim Zin El Abidine El Alaoui
- Fecha Creación: 14/4/2019
- Fecha modificación: 19/4/2019


Versión del desarollo
---------------------
- Versión: 1.1 - Desarollo código para realizar consultas utilizando el plugin KeepassHttp.
- Versión: 1.2 - Se realizar una única consulta a SecureCRT en lugar de dos para obtener el login y password.
- Versión: 1.3 - Se ha mejorado la rutina conexion_session (Fichero vbs) para detectar el prompt en SecureCRT.

