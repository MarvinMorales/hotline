# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /build

# Copia el archivo Pipfile y Pipfile.lock para instalar dependencias
COPY Pipfile Pipfile.lock /build/

# Instala Pipenv y las dependencias del proyecto
RUN pip install pipenv && pipenv install --system --deploy

# Copia el resto de tu aplicación al directorio de trabajo
COPY . /build

# Definir el puerto del servidor como un argumento de compilación con un valor predeterminado de 8000
ARG SERVER_PORT=8000
ENV SERVER_PORT=${SERVER_PORT}

# Expone el puerto en el que se ejecuta tu aplicación FastAPI
EXPOSE ${SERVER_PORT}

# Comando para ejecutar tu aplicación
CMD ["uvicorn", "main:build", "--host", "0.0.0.0", "--port", "${SERVER_PORT}"]