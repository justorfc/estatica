# app_estatica.py

import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt

# Configuración inicial de la página
st.set_page_config(page_title="Aplicativo Estática", layout="wide")

# Título principal
st.title("Aplicativo Interactivo de Estática")
st.markdown("Desarrollado en homenaje al profesor José Arroyo")

# Secciones del menú
menu = st.sidebar.selectbox("Selecciona un módulo:", [
    "Inicio",
    "Cálculo de Reacciones en Vigas",
    "Análisis de Cerchas",
    "Análisis de Cables"
])

# Inicio
if menu == "Inicio":
    st.subheader("Bienvenido")
    st.write("Este aplicativo permite explorar conceptos fundamentales de la estática en los programas de Ingeniería Agrícola y Civil.")
    st.write("Utiliza el menú lateral para acceder a los diferentes módulos.")

# Módulo de Reacciones en Vigas
elif menu == "Cálculo de Reacciones en Vigas":
    st.subheader("Cálculo de Reacciones en Vigas")

    st.markdown("**Ejemplo simplificado:**")
    st.latex(r"\sum M_A = 0\quad\Rightarrow\quad R_B = (F \cdot d) / L")

    F = st.number_input("Fuerza aplicada F (N):", value=100.0)
    d = st.number_input("Distancia desde A hasta la fuerza (m):", value=2.0)
    L = st.number_input("Longitud total de la viga (m):", value=5.0)

    if L != 0:
        RB = F * d / L
        RA = F - RB
        st.write(f"Reacción en A: {RA:.2f} N")
        st.write(f"Reacción en B: {RB:.2f} N")
    else:
        st.error("La longitud de la viga no puede ser cero.")

# Módulo de Cerchas
elif menu == "Análisis de Cerchas":
    st.subheader("Análisis de Cerchas")
    st.info("Módulo en construcción. Próximamente podrás ingresar coordenadas y cargas para obtener fuerzas internas en nodos.")

# Módulo de Cables
elif menu == "Análisis de Cables":
    st.subheader("Análisis de Cables")
    st.info("Este módulo permitirá analizar la tensión en cables suspendidos. En desarrollo.")
