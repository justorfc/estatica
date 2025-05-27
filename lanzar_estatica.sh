#!/bin/bash
echo "Activando entorno virtual..."
source venv/bin/activate
echo "Instalando dependencias (si es necesario)..."
pip install -r requirements.txt
echo "Ejecutando aplicativo..."
streamlit run app_estatica.py
