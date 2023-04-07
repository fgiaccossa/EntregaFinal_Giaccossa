### PROYECTO FINAL PYTHON CODERHOUSE
Se nos propuso crear un blog que permitiera publicar artículos, agregar imágenes, editar y eliminar estos artículos.
También debería tener un programa de mensajería que permitiera comunicarse a los diferentes usuarios del sitio.

#### <u>DESARROLLO</u>
Se trabajó con el framework Django, el IDE Pycharm y se utilizó código de Python 3.9.
Se configuró un sitio de tipo "Landing Page", utilizando como base una plantilla de Bootstrap, donde se configuró un bloque de contenido que cambia, manteniendo siempre la estética del sitio.
<br>Se elaboraron templates HTML para renderizar las vistas de los diferentes modelos.

#### <u>MODULOS</u>
El sitio se basa en la plantilla "index.html" que da un mensaje de bienvenida e introducción al contenido que ofrecerá el blog.
Debajo del mensaje de bienvenida se encuentra un botón "Conoce Mas" que lleva directamente a la funcionalidad de publicaciones.
En la parte superior se encuentra  una barra de navegación que con las siiguientes funcionalidades:

##### Inicio: 
Permite volver a la página de inicio desde cualquier parte del sitio.

##### Acerca de:
Acerca de nos presenta información sobre el proyecto y el sitio.

##### Publicaciones:
Aquí se listan todos los artículos publicados en el blog.
Debajo de cada artículo hay un botón "Leer" que permite leer el contenido del artículo.
En caso de ser un usuario registrado y estar logueado, podrá ademas editar o eliminar artículos.
En la parte superior hay un botón "CREAR NUEVA PUBLICACIÓN" que al hacer click permitirá crear una nueva entrada en el blog.
Para que esto sea posible el usuario debe estar logueado.

#### Contacto:
Despliega un formulario de contacto.
En un primer momento iba a ser la base de la App de mensajería pero debido a que el plazo expiró y no logré desarrollarlo aún, por ahora quedó como formulario de contacto.

#### Registrarse:
Despliega el formulario de registro de usuarios.
En caso de registro exitoso mostrará un mensaje.
En caso de que haya habido algún error también presentará un mensaje.
Esta opción se oculta cuando el usuario inicia sesión.

#### Ingresar:
Permite realizar el Login al sitio.
Una vez se ingresan los datos correctamente se presenta un mensaje de indicando un Login exitoso.
Esta opción se oculta cuando el usuario inicia sesión y en su lugar se presenta un mensaje de "bienvenido usuario..." que permite saber en todo momento si se está logueado o no.

#### Salir: 
Esta opción está oculta mientras no se inicia sesión, solamente se muestra luego de que el usuario haya hecho Login.
Permite realizar el logout del sitio.
Si el Logout se realizó con éxito mostrará un mensaje y se volverán a mostrar lso botones de Registro e Ingresar.

#### <u>ADMINISTRACION</u>
Al ingresar a la url /admin, los superusuarios podrán acceder al panel de administración.

