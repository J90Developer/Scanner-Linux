#!/bin/bash

# Este script lista todos los archivos Python en el sistema Linux
# Requiere permisos de superusuario para acceder a todos los directorios

# Verificar si el script se está ejecutando como root
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, ejecuta este script como root o con sudo."
  exit 1
fi

# Listar todos los archivos Python en el sistema
find / -type f -name "*.py" 2>/dev/null
Allow
Skip