name: Ejecutar informe.py

on:
  workflow_dispatch:
  schedule:
    - cron: '0 8 * * *'  # Todos los días a las 08:00 UTC (10:00 peninsular en verano)

jobs:
  send_report:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del repositorio
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Listar archivos (debug)
        run: ls -R

      - name: Ejecutar script informe.py
        run: python informe.py
