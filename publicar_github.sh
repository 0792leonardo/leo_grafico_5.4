#!/usr/bin/env bash
set -e

echo "=== Publicação do gráfico MP10 no GitHub ==="
read -r -p "URL do repositório GitHub (ex.: https://github.com/usuario/repositorio.git): " REPO

git init
git add .
git commit -m "Publicar gráfico MP10 em Plotly"
git branch -M main
git remote add origin "$REPO"
git push -u origin main

echo
echo "Publicação enviada."
echo "No GitHub, configure: Settings > Pages > Source: GitHub Actions"
