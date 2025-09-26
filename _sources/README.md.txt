# Documentación del Proyecto Sphinx_Basics

Este repositorio contiene la librería de funciones matemáticas y la documentación generada automáticamente con **Sphinx** y publicada en **GitHub Pages** usando **GitHub Actions**.

---

## 1. Clonar el repositorio base

El repositorio original con funciones matemáticas se encuentra en:

[https://github.com/Raxy45/sphinx_basics/tree/main/maths](https://github.com/Raxy45/sphinx_basics/tree/main/maths)

Para clonarlo en tu ordenador:

powershell
git clone https://github.com/Raxy45/sphinx_basics.git
cd sphinx_basics

---

## 2. Configuración de Sphinx

Instalar Sphinx y el tema furo:

powershell
pip install sphinx furo

---

## 3. Inicializar la documentación:

powershell
sphinx-quickstart docs

Esto crea la carpeta docs/ con los archivos iniciales.

---

## 4. Editar docs/conf.py para:

Cambiar el tema a furo:

python
html_theme = 'furo'
Ajustar el sys.path para que encuentre la librería:

python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

---

## 5. Generar la documentación
Generar los archivos .rst de la librería y compilar la documentación:

powershell
sphinx-apidoc -o docs/ maths/
cd docs
python -m sphinx -b html source build/html
El resultado se guarda en docs/build/html.

---

## 6. Probar la documentación localmente

Abrir el archivo generado:

powershell
start docs\build\html\index.html

---

## 7. Configurar GitHub Pages
Subir el proyecto a GitHub con los commits.

Ir a Settings > Pages en el repositorio.

Seleccionar la rama gh-pages.

Guardar los cambios.

---

## 8. Configurar GitHub Actions
Crear el archivo .github/workflows/docs.yml con el siguiente contenido:

yaml

name: Deploy Sphinx Docs

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install sphinx
          pip install sphinx-rtd-theme
          pip install furo
          pip install sphinx-autodoc-typehints

      - name: Build docs
        run: |
          cd docs
          sphinx-build -b html source build/html

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs/build/html

---

## 9. Permisos de GitHub Actions
Ir a:

Settings > Actions > General > Workflow permissions

Seleccionar Read and write permissions.

Habilitar Allow GitHub Actions to create and approve pull requests.

---

## 10. Probar el despliegue automático
Hacer un cambio en cualquier archivo (por ejemplo, un docstring).

Hacer commit y push:

powershell
git add .
git commit -m "Prueba de WorkFlow GitHub ACtions"
git push origin main

Ir a la pestaña Actions en GitHub y verificar que el flujo se ejecute correctamente.