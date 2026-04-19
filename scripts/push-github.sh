#!/bin/bash
set -e

# 1. Verifica que existe el archivo .env
if [ ! -f .env ]; then
    echo "No existe el archivo .env"
    exit 1
fi

# 2. Carga las variables del .env (como GITHUB_REPO_URL)
source .env

# 3. Inicializa git si no existe (solo la primera vez)
if [ ! -d .git ]; then
    git init
fi

# 4. Agrega TODOS los archivos al "staging area"
git add .

# 5. Crea un "commit" (una foto del estado actual)
git commit -m "Proyecto full stack con Docker, Compose, Kubernetes y Bash"

# 6. Cambia el nombre de la rama a "main"
git branch -M main

# 7. Conecta tu proyecto local con GitHub
git remote add origin "$GITHUB_REPO_URL"

# 8. Sube todo a GitHub
git push -u origin main
