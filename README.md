
## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd TiendaOnline
    ```
3. Crea un entorno virtual:
    ```sh
    python -m venv env
    ```
4. Activa el entorno virtual:
    - En Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source env/bin/activate
        ```
5. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```
6. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

## Uso

1. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```
2. Abre tu navegador y navega a [http://127.0.0.1:8000/](http://_vscodecontentref_/23) para ver la aplicación en funcionamiento.

## Funcionalidades

- **Gestión de Clientes**: Permite agregar, editar y eliminar clientes.
- **Gestión de Artículos**: Permite agregar, editar y eliminar artículos.
- **Gestión de Pedidos**: Permite agregar, editar y eliminar pedidos.
- **Formulario de Contacto**: Permite a los usuarios enviar mensajes de contacto.
- **Búsqueda de Productos**: Permite a los usuarios buscar productos por nombre.

## Archivos Principales

- [models.py](http://_vscodecontentref_/24): Define los modelos de la aplicación.
- [views.py](http://_vscodecontentref_/25): Define las vistas de la aplicación.
- [forms.py](http://_vscodecontentref_/26): Define los formularios de la aplicación.
- [settings.py](http://_vscodecontentref_/27): Configuración del proyecto Django.
- [urls.py](http://_vscodecontentref_/28): Define las rutas de la aplicación.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
