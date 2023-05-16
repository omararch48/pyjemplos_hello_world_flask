# Hello World Flask

Flask es uno de los frameworks más populares de Python, este ejemplo es una pequeña introducción al uso de este framework en el cual sólo se explica la instalación y escritura de la primera vista en Flask.

## Ejecución

Antes de comenzar, consultando la documentación de flask, debemos observar que para la versión `2.3` de flask se necesita tener instalada una versión igual o superior a la `3.8` de python.

Al ser flask un framework de python que no se encuentra dentro de la librería estandar del lenguaje, se requiere una instalación. Preferentemente flask debe instalarse dentro de un ambiente virtual, para esto debe ejecutarse el siguiente comando
<pre>
    <code>
        python -m venv .flask_env
    </code>
</pre>
la palabra <code>.flask_env</code> corresponde al nombre del ambiente vitual, el punto en el nombre es usado para mostrar la carpeta generada como un archivo oculto.

Para ejecutar este ejemplo de código, deben seguirse los siguientes pasos

1. Clonar o descargar el repositorio y activar el ambiente virtual después de haber sido creado

2. Posicionarse en el repositorio

3. Usar el archivo <code>requeriments.txt</code> para instalar Flask y los paquetes necesarios en las versiones indicadas para evitar problemas de compatibilidad

4. Ejecutar el comando
    <pre>
        <code>flask --app hello run</code>
    </pre>

Esto iniciara un servidor de desarrollo por defecto en `http://localhost:5000` en donde se podrán ver las rutas de la aplicación.