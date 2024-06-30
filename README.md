
## Despliegue del Backend con Docker

1. Navega al directorio del backend:

    ```bash
    cd backend
    ```

2. Construye la imagen de Docker:

    ```bash
    docker build -t backend .
    ```

3. Ejecuta el contenedor:

    ```bash
    docker run -d -p 8000:8000 backend
    ```

4. La API estará disponible en `http://127.0.0.1:8000`.

## Despliegue del Frontend con Docker

1. Navega al directorio del frontend:

    ```bash
    cd frontend
    ```

2. Construye la imagen de Docker:

    ```bash
    docker build -t frontend .
    ```

3. Ejecuta el contenedor:

    ```bash
    docker run -d -p 80:80 frontend
    ```

4. La aplicación estará disponible en `http://localhost:80`.

## Contribuir

Si deseas contribuir a este proyecto, por favor, realiza un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

