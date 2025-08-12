# Usa una imagen base con Python 3.11
FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Exponer el puerto
EXPOSE 8080

# Comando de arranque
CMD ["python", "app.py"]
