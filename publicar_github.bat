@echo off
echo === Publicacao do grafico MP10 no GitHub ===
echo.
set /p REPO=Digite a URL do repositorio GitHub (ex.: https://github.com/usuario/repositorio.git):
git init
git add .
git commit -m "Publicar grafico MP10 em Plotly"
git branch -M main
git remote add origin %REPO%
git push -u origin main
echo.
echo Publicacao enviada. Configure GitHub Pages em:
echo Settings ^> Pages ^> Source: GitHub Actions
pause
