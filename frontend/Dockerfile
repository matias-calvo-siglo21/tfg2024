# Etapa 1: Construcción de la aplicación
FROM node:14 AS build

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto de los archivos de la aplicación
COPY . .

# Construir la aplicación
RUN npm run build

# Etapa 2: Servir la aplicación usando Nginx
FROM nginx:alpine

# Copiar los archivos construidos de la etapa anterior
COPY --from=build /app/build /usr/share/nginx/html

# Copiar configuración personalizada de Nginx si es necesario
# COPY nginx.conf /etc/nginx/nginx.conf

# Exponer el puerto 80
EXPOSE 80

# Comando por defecto para correr Nginx
CMD ["nginx", "-g", "daemon off;"]

